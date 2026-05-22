import argparse
import json
import sys
from pathlib import Path


class TodoError(Exception):
    """Raised when TODO data or user input is invalid."""


def load_todos(path):
    path = Path(path)
    if not path.exists():
        return []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise TodoError(f"Invalid TODO file: {path}") from exc

    if not isinstance(data, list):
        raise TodoError(f"Invalid TODO file: {path}")

    for item in data:
        if not _is_valid_item(item):
            raise TodoError(f"Invalid TODO file: {path}")

    return data


def _is_valid_item(item):
    return (
        isinstance(item, dict)
        and isinstance(item.get("id"), int)
        and not isinstance(item.get("id"), bool)
        and item["id"] > 0
        and isinstance(item.get("title"), str)
        and bool(item["title"].strip())
        and isinstance(item.get("done"), bool)
    )


def save_todos(path, todos):
    """Persist TODO items as formatted JSON."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(todos, indent=2) + "\n", encoding="utf-8")


def add_todo(path, title):
    normalized_title = title.strip()
    if not normalized_title:
        raise TodoError("TODO title cannot be empty")

    todos = load_todos(path)
    next_id = max((item["id"] for item in todos), default=0) + 1
    item = {"id": next_id, "title": normalized_title, "done": False}
    todos.append(item)
    save_todos(path, todos)
    return item


def mark_done(path, todo_id):
    todos = load_todos(path)
    for item in todos:
        if item["id"] == todo_id:
            item["done"] = True
            save_todos(path, todos)
            return item

    raise TodoError(f"No TODO item with id {todo_id}")


def format_todos(todos):
    """Format TODO items for CLI output."""
    if not todos:
        return "No TODO items."

    lines = []
    for item in todos:
        status = "x" if item["done"] else " "
        lines.append(f"[{status}] #{item['id']} {item['title']}")
    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(description="Minimal TODO CLI")
    parser.add_argument("--file", required=True, help="Path to TODO JSON file")

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a TODO item")
    add_parser.add_argument("title")

    subparsers.add_parser("list", help="List TODO items")

    done_parser = subparsers.add_parser("done", help="Mark a TODO item done")
    done_parser.add_argument("todo_id", type=int)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    path = Path(args.file)

    try:
        if args.command == "add":
            item = add_todo(path, args.title)
            print(f"Added #{item['id']}: {item['title']}")
            return 0

        if args.command == "list":
            print(format_todos(load_todos(path)))
            return 0

        if args.command == "done":
            item = mark_done(path, args.todo_id)
            print(f"Done #{item['id']}: {item['title']}")
            return 0
    except TodoError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
