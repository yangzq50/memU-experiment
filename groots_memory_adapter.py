"""
Groots memory experiment adapter.

The benchmark-side code in this file does not reimplement Groots memory. It
invokes the TypeScript fixture in the sibling `groots` repo, which imports and
runs the real `SpaceMemoryService` implementation.

Contract under test:

    retrieve() before generation, memorize() after the turn.
"""

from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Protocol


DEFAULT_GROOTS_REPO = Path(__file__).resolve().parents[1] / "groots"


@dataclass(frozen=True)
class GrootsMemorySnippet:
    id: str
    space_id: str
    summary: str
    memory_type: str = "knowledge"
    score: float = 0.0
    metadata: Dict[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class GrootsMemoryRetrieval:
    context_block: Optional[str]
    snippets: List[GrootsMemorySnippet]


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
    ) -> GrootsMemoryRetrieval:
        ...

    def memorize(self, turn: GrootsMemoryTurn) -> int:
        ...


class GrootsTypeScriptMemoryBackend:
    """
    Subprocess bridge to Groots' real TypeScript memory service.

    The fixture stores records in JSON so experiments can run without a live
    Cloudflare D1 binding. Retrieval/extraction/context formatting still come
    from Groots TypeScript modules.
    """

    def __init__(
        self,
        storage_path: str | Path,
        *,
        enabled_space_ids: Optional[List[str]] = None,
        groots_repo: str | Path | None = None,
    ):
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self.enabled_space_ids = enabled_space_ids or ["experiment-space"]
        self.groots_repo = Path(groots_repo or os.getenv("GROOTS_REPO_PATH") or DEFAULT_GROOTS_REPO)
        self.fixture_path = self.groots_repo / "apps/api/bin/space-memory-fixture.ts"

    def _run_fixture(self, payload: Dict[str, object]) -> Dict[str, object]:
        if not self.fixture_path.exists():
            raise FileNotFoundError(f"Groots memory fixture not found: {self.fixture_path}")

        command = ["bun", "run", str(self.fixture_path)]
        completed = subprocess.run(
            command,
            cwd=self.groots_repo,
            input=json.dumps(payload),
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                "Groots memory fixture failed\n"
                f"command: {' '.join(command)}\n"
                f"stdout: {completed.stdout}\n"
                f"stderr: {completed.stderr}"
            )

        return json.loads(completed.stdout)

    def reset(self) -> None:
        self._run_fixture(
            {
                "command": "reset",
                "storagePath": str(self.storage_path),
            }
        )

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
    ) -> GrootsMemoryRetrieval:
        del top_k

        response = self._run_fixture(
            {
                "command": "retrieve",
                "enabledSpaceIds": self.enabled_space_ids,
                "request": {
                    "agentId": agent_id,
                    "organizationId": organization_id,
                    "prompt": prompt,
                    "sessionId": session_id,
                    "sessionRunId": session_run_id,
                    "spaceIds": space_ids,
                },
                "storagePath": str(self.storage_path),
            }
        )
        items = response.get("items", [])

        return GrootsMemoryRetrieval(
            context_block=response.get("contextBlock"),
            snippets=[
                GrootsMemorySnippet(
                    id=str(item["id"]),
                    memory_type=str(item.get("memoryType", "knowledge")),
                    metadata=dict(item.get("metadata", {})),
                    score=float(item.get("score", 0.0)),
                    space_id=str(item["spaceId"]),
                    summary=str(item["displayText"]),
                )
                for item in items
            ],
        )

    def memorize(self, turn: GrootsMemoryTurn) -> int:
        response = self._run_fixture(
            {
                "command": "memorizeTurn",
                "enabledSpaceIds": self.enabled_space_ids,
                "storagePath": str(self.storage_path),
                "turn": {
                    "agentId": turn.agent_id,
                    "assistantText": turn.assistant_text,
                    "organizationId": turn.organization_id,
                    "sessionId": turn.session_id,
                    "sessionRunId": turn.session_run_id,
                    "spaceIds": turn.space_ids,
                    "userText": turn.user_text,
                },
            }
        )
        return int(response["searchDocumentCount"])

    def memorize_space_file(
        self,
        *,
        content_text: str,
        entry_id: str,
        organization_id: str,
        path: str,
        space_id: str,
        title: Optional[str] = None,
        version: str = "1",
    ) -> int:
        response = self._run_fixture(
            {
                "command": "memorizeSpaceFile",
                "enabledSpaceIds": self.enabled_space_ids,
                "input": {
                    "contentText": content_text,
                    "entryId": entry_id,
                    "organizationId": organization_id,
                    "path": path,
                    "spaceId": space_id,
                    "title": title,
                    "version": version,
                },
                "storagePath": str(self.storage_path),
            }
        )
        return int(response["searchDocumentCount"])


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
        retrieval = self.backend.retrieve(
            agent_id=agent_id,
            organization_id=organization_id,
            prompt=prompt,
            session_id=session_id,
            session_run_id=session_run_id,
            space_ids=space_ids,
            top_k=top_k,
        )
        if not retrieval.context_block:
            return prompt

        return f"{retrieval.context_block}\n\n<user_request>\n{prompt}\n</user_request>"

    def memorize_after_turn(self, turn: GrootsMemoryTurn) -> int:
        return self.backend.memorize(turn)
