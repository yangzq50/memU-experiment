from __future__ import annotations

import argparse
from pathlib import Path

from benchmark_report import write_comparison_report, write_single_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate readable Markdown benchmark reports.")
    parser.add_argument("json_files", nargs="+", help="Benchmark JSON files to include.")
    parser.add_argument(
        "--output",
        default=".tmp/reports/groots-memory-comparison.md",
        help="Markdown comparison report path.",
    )
    parser.add_argument(
        "--single",
        action="store_true",
        help="Also generate one Markdown report next to each input JSON file.",
    )
    args = parser.parse_args()

    if args.single:
        for json_file in args.json_files:
            path = write_single_report(json_file)
            print(f"Wrote single report: {path}")

    output = write_comparison_report(args.json_files, Path(args.output))
    print(f"Wrote comparison report: {output}")


if __name__ == "__main__":
    main()
