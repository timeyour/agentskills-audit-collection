import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from examples.todo_cli.todo import (
    TodoError,
    add_todo,
    format_todos,
    load_todos,
    mark_done,
)


class TodoStoreTests(unittest.TestCase):
    def test_missing_file_loads_empty_list(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "todos.json"

            self.assertEqual(load_todos(path), [])

    def test_add_persists_pending_item_with_incrementing_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "todos.json"

            first = add_todo(path, "write spec")
            second = add_todo(path, "write test")

            self.assertEqual(first["id"], 1)
            self.assertEqual(second["id"], 2)
            self.assertFalse(first["done"])
            self.assertEqual(load_todos(path), [first, second])

    def test_add_rejects_empty_title(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "todos.json"

            with self.assertRaises(TodoError):
                add_todo(path, "  ")

    def test_mark_done_updates_existing_item(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "todos.json"
            item = add_todo(path, "review behavior")

            updated = mark_done(path, item["id"])

            self.assertTrue(updated["done"])
            self.assertTrue(load_todos(path)[0]["done"])

    def test_mark_done_rejects_missing_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "todos.json"

            with self.assertRaises(TodoError):
                mark_done(path, 99)

    def test_corrupt_json_raises_clear_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "todos.json"
            path.write_text("{not json", encoding="utf-8")

            with self.assertRaisesRegex(TodoError, "Invalid TODO file"):
                load_todos(path)

    def test_invalid_item_shape_raises_clear_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "todos.json"
            path.write_text(json.dumps([{"id": "one"}]), encoding="utf-8")

            with self.assertRaisesRegex(TodoError, "Invalid TODO file"):
                load_todos(path)


class TodoCliTests(unittest.TestCase):
    def test_cli_add_list_done_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "todos.json"
            cmd = [sys.executable, "-m", "examples.todo_cli.todo", "--file", str(path)]

            add_result = subprocess.run(
                [*cmd, "add", "ship validation"],
                check=True,
                text=True,
                capture_output=True,
            )
            self.assertIn("Added #1", add_result.stdout)

            list_result = subprocess.run(
                [*cmd, "list"],
                check=True,
                text=True,
                capture_output=True,
            )
            self.assertIn("[ ] #1 ship validation", list_result.stdout)

            done_result = subprocess.run(
                [*cmd, "done", "1"],
                check=True,
                text=True,
                capture_output=True,
            )
            self.assertIn("Done #1", done_result.stdout)

            final_list = subprocess.run(
                [*cmd, "list"],
                check=True,
                text=True,
                capture_output=True,
            )
            self.assertIn("[x] #1 ship validation", final_list.stdout)

    def test_cli_missing_id_exits_nonzero(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "todos.json"
            cmd = [
                sys.executable,
                "-m",
                "examples.todo_cli.todo",
                "--file",
                str(path),
                "done",
                "404",
            ]

            result = subprocess.run(cmd, text=True, capture_output=True)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("No TODO item with id 404", result.stderr)


class TodoFormattingTests(unittest.TestCase):
    def test_format_empty_and_nonempty_lists(self):
        self.assertEqual(format_todos([]), "No TODO items.")

        output = format_todos(
            [
                {"id": 1, "title": "write spec", "done": False},
                {"id": 2, "title": "review", "done": True},
            ]
        )

        self.assertEqual(output, "[ ] #1 write spec\n[x] #2 review")


if __name__ == "__main__":
    unittest.main()
