import importlib.util
import threading
import unittest
import urllib.error
import urllib.parse
import urllib.request
from http.cookiejar import CookieJar
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP_PATH = ROOT / "examples" / "physical-flow-demo" / "app.py"


def load_demo_app():
    spec = importlib.util.spec_from_file_location("physical_flow_demo_app", APP_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PhysicalFlowDemoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = load_demo_app()
        cls.server = cls.app.ThreadingHTTPServer(("127.0.0.1", 0), cls.app.DemoHandler)
        cls.base_url = f"http://127.0.0.1:{cls.server.server_address[1]}"
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def open(self, path, opener=None, data=None):
        request = urllib.request.Request(f"{self.base_url}{path}", data=data)
        if opener:
            return opener.open(request, timeout=5)
        return urllib.request.urlopen(request, timeout=5)

    def test_homepage_renders_cta(self):
        with self.open("/") as response:
            body = response.read().decode("utf-8")

        self.assertEqual(response.status, 200)
        self.assertIn("Physical Flow Test Demo", body)
        self.assertIn("Get Started", body)

    def test_dashboard_requires_login(self):
        with self.open("/dashboard") as response:
            body = response.read().decode("utf-8")

        self.assertEqual(response.status, 200)
        self.assertIn("Sign in", body)

    def test_invalid_delete_task_id_returns_bad_request(self):
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(CookieJar()))
        credentials = urllib.parse.urlencode(
            {"username": self.app.TEST_USER, "password": self.app.TEST_PASS}
        ).encode("utf-8")
        with self.open("/login", opener=opener, data=credentials) as response:
            self.assertEqual(response.status, 200)
            self.assertIn("Dashboard", response.read().decode("utf-8"))

        with self.assertRaises(urllib.error.HTTPError) as context:
            self.open("/delete-task/abc", opener=opener, data=b"")

        self.assertEqual(context.exception.code, 400)
        self.assertIn("Invalid task id", context.exception.read().decode("utf-8"))

    def test_oversized_form_body_returns_payload_too_large(self):
        payload = b"x" * (self.app.MAX_FORM_BYTES + 1)

        with self.assertRaises(urllib.error.HTTPError) as context:
            self.open("/login", data=payload)

        self.assertEqual(context.exception.code, 413)
        self.assertIn("Form body is too large", context.exception.read().decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
