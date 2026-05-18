import json
import os
import tempfile
import threading
import unittest
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from groots_memory_adapter import (
    GrootsMemoryExperimentAgent,
    GrootsMemoryTurn,
    GrootsTypeScriptMemoryBackend,
)


class _MemoryLlmHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        payload = json.loads(self.rfile.read(length).decode("utf-8"))
        prompt = payload["messages"][1]["content"]
        if "Create a compact contextual header" in prompt:
            content = {"contextualText": "This source says Atlas release support belongs to platform."}
        elif "Build a concise" in prompt:
            content = {"summary": "- Atlas release support belongs to platform."}
        elif "Create one compact searchText" in prompt:
            content = {"searchText": f"{prompt} Atlas release platform support"}
        else:
            content = {
                "items": [
                    {
                        "categoryNames": ["knowledge_base" if "space_file" in prompt else "people_profile"],
                        "confidence": 0.95,
                        "entities": ["Atlas", "platform"],
                        "happenedAtIso": None,
                        "keywords": ["Atlas", "release", "platform"],
                        "memoryType": "knowledge" if "space_file" in prompt else "profile",
                        "summary": "Atlas release support belongs to platform.",
                    }
                ]
            }

        body = json.dumps({"choices": [{"message": {"content": json.dumps(content)}}]}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


@contextmanager
def fake_memory_llm_env():
    server = ThreadingHTTPServer(("127.0.0.1", 0), _MemoryLlmHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    old = {
        "GROOTS_MEMORY_API_KEY": os.environ.get("GROOTS_MEMORY_API_KEY"),
        "GROOTS_MEMORY_BASE_URL": os.environ.get("GROOTS_MEMORY_BASE_URL"),
        "GROOTS_MEMORY_MODEL": os.environ.get("GROOTS_MEMORY_MODEL"),
    }
    thread.start()
    os.environ["GROOTS_MEMORY_API_KEY"] = "test-key"
    os.environ["GROOTS_MEMORY_BASE_URL"] = f"http://127.0.0.1:{server.server_port}"
    os.environ["GROOTS_MEMORY_MODEL"] = "test-model"
    try:
        yield
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
        for key, value in old.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


class GrootsMemoryAdapterTest(unittest.TestCase):
    def test_retrieve_before_generation_injects_relevant_memory(self):
        with fake_memory_llm_env(), tempfile.TemporaryDirectory() as directory:
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
        with fake_memory_llm_env(), tempfile.TemporaryDirectory() as directory:
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
        with fake_memory_llm_env(), tempfile.TemporaryDirectory() as directory:
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
