"""Reference tests: all references exist, mention key facts, cross-link."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCES = [
    "architecture", "capabilities", "installation", "configuration",
    "cli-reference", "security-workflows", "vulnerability-analysis",
    "cve-reference", "kubernetes-security", "reporting",
    "troubleshooting", "compatibility", "safety-policy",
    "limitations", "attribution",
]


class TestReferences(unittest.TestCase):
    def test_all_exist_and_nonempty(self) -> None:
        for name in REFERENCES:
            with self.subTest(ref=name):
                path = ROOT / "references" / f"{name}.md"
                self.assertTrue(path.is_file())
                self.assertGreater(path.stat().st_size, 200)

    def test_cli_reference_documents_flags(self) -> None:
        text = (ROOT / "references" / "cli-reference.md").read_text(encoding="utf-8")
        for flag in ("--target", "--output-format", "--severity-threshold",
                     "--dry-run", "--list-modules", "tui"):
            self.assertIn(flag, text)

    def test_capabilities_lists_tool_groups(self) -> None:
        text = (ROOT / "references" / "capabilities.md").read_text(encoding="utf-8")
        for group in ("agents_graph", "k8s_scanner", "prompt_injection",
                      "wrappers", "nuclei", "zap"):
            self.assertIn(group, text)

    def test_attribution_links(self) -> None:
        text = (ROOT / "references" / "attribution.md").read_text(encoding="utf-8")
        self.assertIn("https://github.com/hleliofficiel/ExaAiAgent", text)
        self.assertIn("https://github.com/hleliofficiel/ExaAiAgent-Skill", text)

    def test_safety_policy_authorized_only(self) -> None:
        text = (ROOT / "references" / "safety-policy.md").read_text(encoding="utf-8")
        self.assertIn("authorized", text.lower())
        self.assertIn("blocklist", text.lower())

    def test_skill_links_all_references(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for name in REFERENCES:
            self.assertIn(f"references/{name}.md", skill)


if __name__ == "__main__":
    unittest.main()
