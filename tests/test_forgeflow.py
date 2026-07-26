from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "forgeflow-init.py"
SKILLS = ROOT / "plugins" / "forgeflow" / "skills"


class InstallerTests(unittest.TestCase):
    def run_installer(self, target: str, project: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(INSTALLER), target, "--project", str(project)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_all_supported_targets_install_and_refuse_overwrite(self) -> None:
        expected = {
            "agents": "AGENTS.md",
            "claude": ".claude/rules/forgeflow.md",
            "cursor": ".cursor/rules/forgeflow.mdc",
            "windsurf": ".devin/rules/forgeflow.md",
            "copilot": ".github/instructions/forgeflow.instructions.md",
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for target, relative in expected.items():
                with self.subTest(target=target):
                    project = root / target
                    project.mkdir()
                    first = self.run_installer(target, project)
                    self.assertEqual(first.returncode, 0, first.stderr)
                    self.assertTrue((project / relative).is_file())

                    second = self.run_installer(target, project)
                    self.assertEqual(second.returncode, 2)
                    self.assertIn("Refusing to overwrite", second.stderr)

    @unittest.skipIf(os.name == "nt", "symlink creation is not normally available on Windows")
    def test_dangling_destination_symlink_cannot_escape_project(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            project = root / "project"
            rules = project / ".claude" / "rules"
            rules.mkdir(parents=True)
            outside = root / "outside.md"
            (rules / "forgeflow.md").symlink_to(outside)

            result = self.run_installer("claude", project)

            self.assertEqual(result.returncode, 3)
            self.assertIn("symbolic link", result.stderr)
            self.assertFalse(outside.exists())

    @unittest.skipIf(os.name == "nt", "symlink creation is not normally available on Windows")
    def test_parent_symlink_cannot_escape_project(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            project = root / "project"
            outside = root / "outside"
            project.mkdir()
            outside.mkdir()
            (project / ".claude").symlink_to(outside, target_is_directory=True)

            result = self.run_installer("claude", project)

            self.assertEqual(result.returncode, 3)
            self.assertIn("symbolic link", result.stderr)
            self.assertFalse((outside / "rules" / "forgeflow.md").exists())


class WorkflowContractTests(unittest.TestCase):
    def test_every_skill_has_valid_basic_frontmatter(self) -> None:
        for skill_file in sorted(SKILLS.glob("*/SKILL.md")):
            with self.subTest(skill=skill_file.parent.name):
                lines = skill_file.read_text(encoding="utf-8").splitlines()
                self.assertGreaterEqual(len(lines), 4)
                self.assertEqual(lines[0], "---")
                self.assertTrue(lines[1].startswith("name: "))
                self.assertTrue(lines[2].startswith("description: "))
                self.assertEqual(lines[3], "---")

    def test_no_magic_approval_phrase_remains(self) -> None:
        checked = [ROOT / "README.md", ROOT / "adapters" / "README.md", ROOT / "core" / "FORGEFLOW.md"]
        checked.extend(SKILLS.glob("*/SKILL.md"))
        checked.append(SKILLS / "forgeflow" / "references" / "state-template.md")
        for path in checked:
            with self.subTest(path=path):
                self.assertNotIn("Approve next:", path.read_text(encoding="utf-8"))

    def test_handoff_skills_accept_natural_confirmation_and_stop(self) -> None:
        handoff_skills = [
            "brainstorming",
            "grill-with-docs",
            "wayfinder",
            "to-spec",
            "implementation-plan",
            "to-tickets",
            "tdd",
            "implement",
            "parallel-execution",
        ]
        for name in handoff_skills:
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8").lower()
            with self.subTest(skill=name):
                self.assertIn("clear affirmative", text)
                self.assertIn("stop", text)

    def test_portable_core_is_dormant_until_invoked(self) -> None:
        text = (ROOT / "core" / "FORGEFLOW.md").read_text(encoding="utf-8").lower()
        self.assertIn("activation boundary", text)
        self.assertIn("dormant unless the user explicitly starts or resumes forgeflow", text)
        self.assertIn("approve", text)
        self.assertIn("go ahead", text)

    def test_wayfinder_is_local_and_has_no_missing_upstream_commands(self) -> None:
        text = (SKILLS / "wayfinder" / "SKILL.md").read_text(encoding="utf-8")
        for stale_reference in (
            "/setup-matt-pocock-skills",
            "/grilling",
            "/domain-modeling",
            "/research",
            "canonical artifact",
        ):
            with self.subTest(reference=stale_reference):
                self.assertNotIn(stale_reference, text)
        self.assertIn("Everything is local by default", text)
        self.assertIn("## Completion gate", text)

    def test_visual_companion_does_not_load_remote_branding(self) -> None:
        server = (SKILLS / "brainstorming" / "scripts" / "server.cjs").read_text(encoding="utf-8")
        self.assertNotIn("primeradiant.com", server)
        self.assertNotIn("cp.exec(", server)
        self.assertIn("default-src 'self' data:", server)

    def test_explicit_browser_choice_uses_persisted_choice_field(self) -> None:
        helper = (SKILLS / "brainstorming" / "scripts" / "helper.js").read_text(encoding="utf-8")
        self.assertIn("...metadata, type: 'choice', choice: value", helper)

    def test_manifest_is_valid_and_versioned(self) -> None:
        manifest = json.loads(
            (ROOT / "plugins" / "forgeflow" / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        self.assertEqual(manifest["name"], "forgeflow")
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")


class VisualCompanionScriptTests(unittest.TestCase):
    @unittest.skipIf(os.name == "nt", "shell and symlink behavior is covered by Unix CI")
    def test_project_state_symlink_is_rejected(self) -> None:
        script = SKILLS / "brainstorming" / "scripts" / "start-server.sh"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            project = root / "project"
            outside = root / "outside"
            project.mkdir()
            outside.mkdir()
            (project / ".superpowers").symlink_to(outside, target_is_directory=True)

            result = subprocess.run(
                ["bash", str(script), "--project-dir", str(project)],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 1)
            self.assertIn("Refusing to follow symbolic link", result.stdout)
            self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
