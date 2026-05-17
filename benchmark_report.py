from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


LOCOMO_CATEGORY_LABELS = {
    "1": "single-hop",
    "2": "temporal",
    "3": "multi-hop",
    "4": "open-domain",
    "5": "adversarial",
}


def category_label(category: object) -> str:
    key = str(category)
    label = LOCOMO_CATEGORY_LABELS.get(key)
    return f"{key} ({label})" if label else key


def _as_percent(value: float | int | None) -> str:
    if not isinstance(value, int | float):
        return "n/a"
    return f"{value:.2%}"


def _as_seconds(value: float | int | None) -> str:
    if not isinstance(value, int | float):
        return "n/a"
    if value < 120:
        return f"{value:.1f}s"
    return f"{value / 60:.1f}m"


def _escape_cell(value: object) -> str:
    return str(value).replace("\n", " ").replace("|", "\\|")


def _table(headers: list[str], rows: Iterable[Iterable[object]]) -> str:
    output = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        output.append("| " + " | ".join(_escape_cell(value) for value in row) + " |")
    return "\n".join(output)


def load_result(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as file:
        result = json.load(file)
    if not isinstance(result, dict):
        raise ValueError(f"Benchmark result is not a JSON object: {path}")
    return result


def backend_label(result: dict[str, Any]) -> str:
    args = result.get("args", {})
    if not isinstance(args, dict):
        return "unknown"
    backend = args.get("memory_backend", "unknown")
    if backend == "memu" and args.get("disable_embeddings"):
        return "memu-text"
    return str(backend)


def result_title(result: dict[str, Any]) -> str:
    args = result.get("args", {})
    if not isinstance(args, dict):
        return backend_label(result)
    return (
        f"{backend_label(result)} / {args.get('chat_deployment', 'unknown-model')} / "
        f"sample={args.get('sample_use', 'all')} / category={args.get('category', 'all')}"
    )


def _question_results(result: dict[str, Any]) -> list[dict[str, Any]]:
    detailed = result.get("detailed_results", [])
    questions: list[dict[str, Any]] = []
    if not isinstance(detailed, list):
        return questions
    for sample in detailed:
        if isinstance(sample, dict) and isinstance(sample.get("question_results"), list):
            questions.extend(item for item in sample["question_results"] if isinstance(item, dict))
    return questions


def _wrong_examples(result: dict[str, Any], limit: int = 5) -> list[dict[str, Any]]:
    return [question for question in _question_results(result) if not question.get("is_correct")][:limit]


def evaluated_counts(result: dict[str, Any]) -> tuple[int, int]:
    questions = _question_results(result)
    return sum(1 for question in questions if question.get("is_correct")), len(questions)


def _questions_total(result: dict[str, Any]) -> int | str:
    summary = result.get("summary", {})
    if isinstance(summary, dict) and isinstance(summary.get("total_questions"), int):
        return summary["total_questions"]
    total = 0
    for sample in result.get("detailed_results", []):
        if isinstance(sample, dict) and isinstance(sample.get("questions_total"), int):
            total += sample["questions_total"]
    return total or "n/a"


def _questions_skipped(result: dict[str, Any]) -> int | str:
    total = 0
    found = False
    for sample in result.get("detailed_results", []):
        if isinstance(sample, dict) and isinstance(sample.get("questions_skipped"), int):
            total += sample["questions_skipped"]
            found = True
    return total if found else "n/a"


def render_single_report(result: dict[str, Any], *, source_path: str | Path | None = None) -> str:
    args = result.get("args", {})
    summary = result.get("summary", {})
    if not isinstance(args, dict):
        args = {}
    if not isinstance(summary, dict):
        summary = {}
    correct_count, evaluated_count = evaluated_counts(result)

    category_stats = summary.get("category_stats", {})
    category_rows = []
    if isinstance(category_stats, dict):
        for category, stats in sorted(category_stats.items()):
            if isinstance(stats, dict):
                total = int(stats.get("total", 0))
                correct = int(stats.get("correct", 0))
                accuracy = correct / total if total > 0 else 0.0
                category_rows.append([category_label(category), correct, total, _as_percent(accuracy)])

    lines = [
        f"# Benchmark Report: {result_title(result)}",
        "",
        f"- Generated at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- Source JSON: `{source_path}`" if source_path else "- Source JSON: n/a",
        f"- Command: `{result.get('script', 'n/a')}`",
        f"- Backend: `{backend_label(result)}`",
        f"- Chat model: `{args.get('chat_deployment', 'n/a')}`",
        f"- Eval model: `{args.get('eval_deployment', args.get('chat_deployment', 'n/a'))}`",
        f"- Data file: `{args.get('data_file', 'n/a')}`",
        f"- Sample: `{args.get('sample_use', 'all')}`",
        f"- Category: `{category_label(args.get('category')) if args.get('category') else 'all'}`",
        "",
        "## Summary",
        "",
        _table(
            ["Metric", "Value"],
            [
                ["Successful samples", summary.get("successful_samples", "n/a")],
                ["Sessions processed", summary.get("sessions_processed", "n/a")],
                ["Sessions skipped", summary.get("sessions_skipped", "n/a")],
                ["Questions available before filter", _questions_total(result)],
                ["Questions skipped by filter", _questions_skipped(result)],
                ["Questions evaluated", evaluated_count],
                ["Correct answers", f"{correct_count}/{evaluated_count}"],
                ["Overall accuracy", _as_percent(correct_count / evaluated_count if evaluated_count else 0.0)],
                ["Total time", _as_seconds(summary.get("total_time"))],
            ],
        ),
        "",
        "## Category Accuracy",
        "",
        _table(["Category", "Correct", "Total", "Accuracy"], category_rows or [["n/a", "n/a", "n/a", "n/a"]]),
    ]

    wrong_examples = _wrong_examples(result)
    if wrong_examples:
        lines.extend(["", "## Wrong Examples", ""])
        for item in wrong_examples:
            lines.extend(
                [
                    f"### Q{item.get('qa_index', 'n/a')}: {item.get('question', '')}",
                    "",
                    f"- Category: `{category_label(item.get('category', 'n/a'))}`",
                    f"- Generated: {item.get('generated_answer', '')}",
                    f"- Expected: {item.get('standard_answer', '')}",
                    f"- Evaluation: {item.get('explanation', '')}",
                    "",
                ]
            )

    return "\n".join(lines).rstrip() + "\n"


def render_comparison_report(results: list[tuple[Path, dict[str, Any]]]) -> str:
    if not results:
        raise ValueError("No benchmark results were provided.")

    summary_rows = []
    question_sets: dict[str, set[tuple[Any, Any]]] = {}
    wrong_sets: dict[str, set[tuple[Any, Any]]] = {}

    for path, result in results:
        args = result.get("args", {})
        summary = result.get("summary", {})
        if not isinstance(args, dict):
            args = {}
        if not isinstance(summary, dict):
            summary = {}
        label = backend_label(result)
        questions = _question_results(result)
        correct_count, evaluated_count = evaluated_counts(result)
        all_ids = {(question.get("category"), question.get("qa_index")) for question in questions}
        wrong_ids = {
            (question.get("category"), question.get("qa_index"))
            for question in questions
            if not question.get("is_correct")
        }
        question_sets[label] = all_ids
        wrong_sets[label] = wrong_ids

        summary_rows.append(
            [
                label,
                args.get("chat_deployment", "n/a"),
                args.get("eval_deployment", args.get("chat_deployment", "n/a")),
                args.get("sample_use", "all"),
                category_label(args.get("category")) if args.get("category") else "all",
                _questions_total(result),
                _questions_skipped(result),
                evaluated_count,
                f"{correct_count}/{evaluated_count}",
                _as_percent(correct_count / evaluated_count if evaluated_count else 0.0),
                _as_seconds(summary.get("total_time")),
                path.name,
            ]
        )

    lines = [
        "# Groots Memory vs memU Benchmark Report",
        "",
        f"- Generated at: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "- Evaluation uses the JSON result files listed in the table below.",
        "- `Available` is the number of questions in the selected sample before category filtering.",
        "- `Evaluated` is the number of questions actually answered and scored in this run.",
        "",
        "## Headline",
        "",
        _table(
            [
                "Backend",
                "Chat Model",
                "Eval Model",
                "Sample",
                "Category",
                "Available",
                "Skipped",
                "Evaluated",
                "Correct",
                "Accuracy",
                "Time",
                "JSON",
            ],
            summary_rows,
        ),
    ]

    if len(results) >= 2:
        first_label = backend_label(results[0][1])
        second_label = backend_label(results[1][1])
        first_wrong = wrong_sets.get(first_label, set())
        second_wrong = wrong_sets.get(second_label, set())
        shared_questions = question_sets.get(first_label, set()) & question_sets.get(second_label, set())
        lines.extend(
            [
                "",
                "## Error Overlap",
                "",
                _table(
                    ["Metric", "Value"],
                    [
                        ["Shared evaluated questions", len(shared_questions)],
                        [f"Wrong only in {first_label}", len(first_wrong - second_wrong)],
                        [f"Wrong only in {second_label}", len(second_wrong - first_wrong)],
                        ["Wrong in both", len(first_wrong & second_wrong)],
                    ],
                ),
            ]
        )

    lines.extend(["", "## Per-Backend Wrong Examples", ""])
    for path, result in results:
        lines.extend([f"### {backend_label(result)}", ""])
        wrong_examples = _wrong_examples(result, limit=8)
        if not wrong_examples:
            lines.extend(["No wrong examples recorded.", ""])
            continue
        for item in wrong_examples:
            lines.extend(
                [
                    f"- Q{item.get('qa_index', 'n/a')} / {category_label(item.get('category', 'n/a'))}: {item.get('question', '')}",
                    f"  - Generated: {item.get('generated_answer', '')}",
                    f"  - Expected: {item.get('standard_answer', '')}",
                ]
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_single_report(json_path: str | Path, markdown_path: str | Path | None = None) -> Path:
    source = Path(json_path)
    target = Path(markdown_path) if markdown_path else source.with_suffix(".md")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_single_report(load_result(source), source_path=source), encoding="utf-8")
    return target


def write_comparison_report(json_paths: list[str | Path], markdown_path: str | Path) -> Path:
    target = Path(markdown_path)
    loaded = [(Path(path), load_result(path)) for path in json_paths]
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_comparison_report(loaded), encoding="utf-8")
    return target
