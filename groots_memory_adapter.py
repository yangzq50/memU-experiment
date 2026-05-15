"""
Groots memory experiment adapter.

This module gives the LoCoMo experiment code a stable seam for testing the
Groots memory contract without depending on a live Groots API yet:

    retrieve() before generation, memorize() after the turn.

The default backend is a small JSONL text store so benchmark plumbing can be
developed and tested offline. A future HTTP/D1-backed backend can implement the
same interface without changing the experiment runner.
"""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Protocol


TOKEN_PATTERN = re.compile(r"[\w\u4e00-\u9fff]+", re.UNICODE)


def tokenize(text: str) -> List[str]:
    return [token.lower() for token in TOKEN_PATTERN.findall(text)]


@dataclass(frozen=True)
class GrootsMemorySnippet:
    id: str
    space_id: str
    summary: str
    memory_type: str = "knowledge"
    score: float = 0.0
    metadata: Dict[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class GrootsMemoryTurn:
    agent_id: str
    assistant_text: str
    organization_id: str
    session_id: str
    session_run_id: str
    space_ids: List[str]
    user_text: str


class GrootsMemoryBackend(Protocol):
    def retrieve(
        self,
        *,
        agent_id: str,
        organization_id: str,
        prompt: str,
        session_id: str,
        session_run_id: str,
        space_ids: List[str],
        top_k: int = 8,
    ) -> List[GrootsMemorySnippet]:
        ...

    def memorize(self, turn: GrootsMemoryTurn) -> int:
        ...


class JsonlGrootsMemoryBackend:
    """
    Offline text backend for experiment development.

    Records are JSON lines with at least `space_id` and `summary`. Retrieval uses
    a small BM25 implementation, matching Groots' current no-vector-db direction.
    """

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _read_records(self) -> List[Dict[str, object]]:
        if not self.path.exists():
            return []

        records: List[Dict[str, object]] = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            records.append(json.loads(line))
        return records

    def _append_record(self, record: Dict[str, object]) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

    def retrieve(
        self,
        *,
        agent_id: str,
        organization_id: str,
        prompt: str,
        session_id: str,
        session_run_id: str,
        space_ids: List[str],
        top_k: int = 8,
    ) -> List[GrootsMemorySnippet]:
        del agent_id, organization_id, session_id, session_run_id

        records = [
            record
            for record in self._read_records()
            if str(record.get("space_id", "")) in set(space_ids)
        ]
        scored = _bm25(prompt, records)

        return [
            GrootsMemorySnippet(
                id=str(record.get("id", f"memory-{index}")),
                memory_type=str(record.get("memory_type", "knowledge")),
                metadata=dict(record.get("metadata", {})),
                score=score,
                space_id=str(record["space_id"]),
                summary=str(record["summary"]),
            )
            for index, (record, score) in enumerate(scored[:top_k], start=1)
        ]

    def memorize(self, turn: GrootsMemoryTurn) -> int:
        text = "\n".join(
            part
            for part in [
                f"User: {turn.user_text.strip()}",
                f"Assistant: {turn.assistant_text.strip()}",
            ]
            if part.strip()
        )
        if not text.strip():
            return 0

        count = 0
        for space_id in turn.space_ids:
            self._append_record(
                {
                    "id": f"{turn.session_run_id}:{space_id}",
                    "memory_type": "knowledge",
                    "metadata": {
                        "agent_id": turn.agent_id,
                        "organization_id": turn.organization_id,
                        "session_id": turn.session_id,
                        "session_run_id": turn.session_run_id,
                    },
                    "space_id": space_id,
                    "summary": text,
                }
            )
            count += 1
        return count


class GrootsMemoryExperimentAgent:
    def __init__(self, backend: GrootsMemoryBackend):
        self.backend = backend

    def retrieve_before_generation(
        self,
        *,
        agent_id: str,
        organization_id: str,
        prompt: str,
        session_id: str,
        session_run_id: str,
        space_ids: List[str],
        top_k: int = 8,
    ) -> str:
        snippets = self.backend.retrieve(
            agent_id=agent_id,
            organization_id=organization_id,
            prompt=prompt,
            session_id=session_id,
            session_run_id=session_run_id,
            space_ids=space_ids,
            top_k=top_k,
        )
        if not snippets:
            return prompt

        memory_lines = "\n".join(
            f"- [{snippet.memory_type} space={snippet.space_id}] {snippet.summary}"
            for snippet in snippets
        )
        return (
            "<groots_space_memory>\n"
            "Use these snippets only when relevant to the current question.\n"
            f"{memory_lines}\n"
            "</groots_space_memory>\n\n"
            f"<user_request>\n{prompt}\n</user_request>"
        )

    def memorize_after_turn(self, turn: GrootsMemoryTurn) -> int:
        return self.backend.memorize(turn)


def _bm25(query: str, records: Iterable[Dict[str, object]]) -> List[tuple[Dict[str, object], float]]:
    documents = list(records)
    query_terms = set(tokenize(query))
    if not query_terms or not documents:
        return []

    tokenized_docs = [tokenize(str(record.get("summary", ""))) for record in documents]
    avg_len = sum(max(len(tokens), 1) for tokens in tokenized_docs) / len(tokenized_docs)
    document_frequency: Dict[str, int] = {}
    for terms in tokenized_docs:
        for term in set(terms):
            document_frequency[term] = document_frequency.get(term, 0) + 1

    scored: List[tuple[Dict[str, object], float]] = []
    for record, terms in zip(documents, tokenized_docs):
        term_counts: Dict[str, int] = {}
        for term in terms:
            term_counts[term] = term_counts.get(term, 0) + 1

        score = 0.0
        length = max(len(terms), 1)
        for term in query_terms:
            frequency = term_counts.get(term, 0)
            if frequency == 0:
                continue

            containing_docs = document_frequency.get(term, 0)
            idf = math.log(1 + (len(documents) - containing_docs + 0.5) / (containing_docs + 0.5))
            score += idf * ((frequency * 2.2) / (frequency + 1.2 * (0.25 + 0.75 * length / avg_len)))

        if score > 0:
            scored.append((record, score))

    return sorted(scored, key=lambda item: item[1], reverse=True)
