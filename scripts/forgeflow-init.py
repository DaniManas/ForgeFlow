#!/usr/bin/env python3
"""Install Forgeflow's portable workflow into one project's AI instructions."""

from __future__ import annotations

import argparse
import os
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


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def reject_symlink_components(project: Path, relative: Path) -> None:
    current = project
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"Refusing to follow symbolic link: {current}")
        if current.exists() and not is_within(current.resolve(), project):
            raise ValueError(f"Destination escapes project directory: {current}")


def write_new_file_safely(project: Path, relative: Path, content: str) -> Path:
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"Unsafe destination path: {relative}")

    destination = project / relative
    reject_symlink_components(project, relative)

    # lexists detects dangling symlinks, unlike Path.exists().
    if os.path.lexists(destination):
        raise FileExistsError(destination)

    destination.parent.mkdir(parents=True, exist_ok=True)
    reject_symlink_components(project, relative)
    if not is_within(destination.parent.resolve(), project):
        raise ValueError(f"Destination escapes project directory: {destination}")

    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW

    descriptor = os.open(destination, flags, 0o644)
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        handle.write(content)
    return destination


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
    try:
        destination = write_new_file_safely(
            project,
            Path(relative_destination),
            prefix + CORE.read_text(encoding="utf-8"),
        )
    except FileExistsError:
        print(
            f"Refusing to overwrite existing file: {destination}\n"
            "Add Forgeflow manually, or move/remove that file and run this command again.",
            file=sys.stderr,
        )
        return 2
    except (OSError, ValueError) as error:
        print(f"Unable to install Forgeflow safely: {error}", file=sys.stderr)
        return 3

    print(f"Installed Forgeflow for {args.target}: {destination}")
    print("Start a new agent session, then say: Start Forgeflow in Balanced mode.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
