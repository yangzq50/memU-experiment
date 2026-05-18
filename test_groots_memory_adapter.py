import tempfile
import unittest
from pathlib import Path

from groots_memory_adapter import (
    GrootsMemoryExperimentAgent,
    GrootsMemoryTurn,
    GrootsTypeScriptMemoryBackend,
)


class GrootsMemoryAdapterTest(unittest.TestCase):
    def test_retrieve_before_generation_injects_relevant_memory(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "memory.json"
            backend = GrootsTypeScriptMemoryBackend(path, enabled_space_ids=["space-1"])
            backend.memorize(
                GrootsMemoryTurn(
                    agent_id="agent-1",
                    assistant_text="Atlas launch moved to July after API review.",
                    organization_id="org-1",
                    session_id="session-1",
                    session_run_id="run-1",
                    space_ids=["space-1"],
                    user_text="Remember the Atlas launch timing.",
                )
            )
            agent = GrootsMemoryExperimentAgent(backend)

            prompt = agent.retrieve_before_generation(
                agent_id="agent-1",
                organization_id="org-1",
                prompt="When is Atlas launching?",
                session_id="session-1",
                session_run_id="run-2",
                space_ids=["space-1"],
            )

            self.assertIn("groots_space_memory", prompt)
            self.assertIn("Atlas launch moved to July", prompt)
            self.assertIn("<user_request>", prompt)

    def test_memorize_after_turn_indexes_enabled_spaces(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "memory.json"
            backend = GrootsTypeScriptMemoryBackend(path, enabled_space_ids=["space-1", "space-2"])
            agent = GrootsMemoryExperimentAgent(backend)

            count = agent.memorize_after_turn(
                GrootsMemoryTurn(
                    agent_id="agent-1",
                    assistant_text="I will use the release checklist.",
                    organization_id="org-1",
                    session_id="session-1",
                    session_run_id="run-1",
                    space_ids=["space-1", "space-2"],
                    user_text="The release checklist belongs to platform.",
                )
            )

            self.assertGreaterEqual(count, 2)
            content = path.read_text(encoding="utf-8")
            self.assertIn("space-1", content)
            self.assertIn("space-2", content)

    def test_space_file_memory_uses_groots_service(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "memory.json"
            backend = GrootsTypeScriptMemoryBackend(path, enabled_space_ids=["space-1"])

            count = backend.memorize_space_file(
                content_text=(
                    "Atlas deployment notes live here and include rollback steps.\n\n"
                    "The release owner is the platform team."
                ),
                entry_id="entry-1",
                organization_id="org-1",
                path="/Atlas.md",
                space_id="space-1",
            )
            retrieval = backend.retrieve(
                agent_id="agent-1",
                organization_id="org-1",
                prompt="Who owns the Atlas release?",
                session_id="session-1",
                session_run_id="run-1",
                space_ids=["space-1"],
            )

            self.assertGreaterEqual(count, 2)
            self.assertTrue(retrieval.context_block)
            self.assertIn("platform team", retrieval.context_block or "")


if __name__ == "__main__":
    unittest.main()
