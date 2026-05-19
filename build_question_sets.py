from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _load_questions(path: Path) -> dict[int, dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        payload = json.load(file)

    questions: dict[int, dict[str, Any]] = {}
    for sample in payload.get("detailed_results", []):
        if not isinstance(sample, dict):
            continue
        for question in sample.get("question_results", []):
            if not isinstance(question, dict):
                continue
            qa_index = question.get("qa_index")
            if isinstance(qa_index, int):
                questions[qa_index] = question

    return questions


def _write_set(
    output_dir: Path,
    name: str,
    description: str,
    indices: set[int],
    questions: dict[int, dict[str, Any]],
    source_results: list[str],
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    sorted_indices = sorted(indices)
    category_counts: dict[str, int] = {}

    for index in sorted_indices:
        category = str(questions[index].get("category", "Unknown"))
        category_counts[category] = category_counts.get(category, 0) + 1

    payload = {
        "name": name,
        "description": description,
        "sample_use": "[0]",
        "source_results": source_results,
        "count": len(sorted_indices),
        "category_counts": dict(sorted(category_counts.items())),
        "qa_indices": sorted_indices,
    }
    output_path = output_dir / f"{name}.json"
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2, ensure_ascii=False)
        file.write("\n")

    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Build reusable LoCoMo QA index sets from benchmark results.")
    parser.add_argument("--groots-result", required=True, type=Path)
    parser.add_argument("--memu-result", required=True, type=Path)
    parser.add_argument("--output-dir", default=Path("benchmark_sets"), type=Path)
    args = parser.parse_args()

    groots = _load_questions(args.groots_result)
    memu = _load_questions(args.memu_result)
    shared = set(groots) & set(memu)
    groots_wrong = {index for index in shared if not groots[index].get("is_correct")}
    memu_wrong = {index for index in shared if not memu[index].get("is_correct")}
    both_wrong = groots_wrong & memu_wrong
    union_wrong = groots_wrong | memu_wrong
    groots_gap = groots_wrong - memu_wrong
    memu_gap = memu_wrong - groots_wrong
    source_results = [str(args.groots_result), str(args.memu_result)]

    for output_path in [
        _write_set(
            args.output_dir,
            "locomo-s0-error-union-v1",
            "Sample 0 questions missed by either Groots memory or memU in the baseline full benchmark.",
            union_wrong,
            groots,
            source_results,
        ),
        _write_set(
            args.output_dir,
            "locomo-s0-both-wrong-v1",
            "Sample 0 questions missed by both Groots memory and memU in the baseline full benchmark.",
            both_wrong,
            groots,
            source_results,
        ),
        _write_set(
            args.output_dir,
            "locomo-s0-groots-gap-v1",
            "Sample 0 questions missed by Groots memory but answered correctly by memU.",
            groots_gap,
            groots,
            source_results,
        ),
        _write_set(
            args.output_dir,
            "locomo-s0-memu-gap-v1",
            "Sample 0 questions missed by memU but answered correctly by Groots memory.",
            memu_gap,
            groots,
            source_results,
        ),
    ]:
        print(output_path)


if __name__ == "__main__":
    main()
