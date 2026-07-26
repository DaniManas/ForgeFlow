#!/usr/bin/env python3
"""Install Forgeflow's portable workflow into one project's AI instructions."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "core" / "FORGEFLOW.md"

TARGETS = {
    "agents": ("AGENTS.md", ""),
    "claude": (".claude/rules/forgeflow.md", ""),
    "cursor": (
        ".cursor/rules/forgeflow.mdc",
        "---\n"
        "description: Forgeflow approval-first workflow for turning an idea into reviewed code\n"
        "alwaysApply: true\n"
        "---\n\n",
    ),
    "windsurf": (
        ".devin/rules/forgeflow.md",
        "---\n"
        "trigger: always_on\n"
        "---\n\n",
    ),
    "copilot": (
        ".github/instructions/forgeflow.instructions.md",
        "---\n"
        "applyTo: \"**\"\n"
        "---\n\n",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install Forgeflow's portable workflow into a project instruction file."
    )
    parser.add_argument("target", choices=sorted(TARGETS), help="Agent instruction format")
    parser.add_argument(
        "--project",
        type=Path,
        default=Path.cwd(),
        help="Project directory to configure (default: current directory)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not CORE.is_file():
        print(f"Forgeflow core not found: {CORE}", file=sys.stderr)
        return 1

    project = args.project.expanduser().resolve()
    if not project.is_dir():
        print(f"Project directory does not exist: {project}", file=sys.stderr)
        return 1

    relative_destination, prefix = TARGETS[args.target]
    destination = project / relative_destination
    if destination.exists():
        print(
            f"Refusing to overwrite existing file: {destination}\n"
            "Add Forgeflow manually, or move/remove that file and run this command again.",
            file=sys.stderr,
        )
        return 2

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(prefix + CORE.read_text(), encoding="utf-8")
    print(f"Installed Forgeflow for {args.target}: {destination}")
    print("Start a new agent session, then say: Start Forgeflow in Balanced mode.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
