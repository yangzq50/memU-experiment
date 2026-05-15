import tempfile
import unittest
from pathlib import Path

from groots_memory_adapter import (
    GrootsMemoryExperimentAgent,
    GrootsMemoryTurn,
    JsonlGrootsMemoryBackend,
)


class GrootsMemoryAdapterTest(unittest.TestCase):
    def test_retrieve_before_generation_injects_relevant_memory(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "memory.jsonl"
            backend = JsonlGrootsMemoryBackend(path)
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

    def test_memorize_after_turn_appends_one_record_per_space(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "memory.jsonl"
            backend = JsonlGrootsMemoryBackend(path)
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

            self.assertEqual(count, 2)
            lines = path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lines), 2)
            self.assertIn("space-1", lines[0])
            self.assertIn("space-2", lines[1])


if __name__ == "__main__":
    unittest.main()
