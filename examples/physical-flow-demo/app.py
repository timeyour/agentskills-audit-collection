from http import cookies
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
import html
import secrets


HOST = "127.0.0.1"
PORT = 5000
TEST_USER = "test_user"
TEST_PASS = "test_pass"

sessions = {}
tasks = [
    {"id": 1, "title": "Review homepage CTA"},
    {"id": 2, "title": "Verify login failure state"},
]
next_task_id = 3


def page(title, body, status=200):
    return status, f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} - Physical Flow Demo</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 0; color: #17202a; background: #f7f9fb; }}
    header {{ background: #103b5b; color: white; padding: 16px 24px; }}
    nav a {{ color: white; margin-right: 16px; }}
    main {{ max-width: 840px; margin: 40px auto; padding: 0 20px; }}
    .panel {{ background: white; border: 1px solid #d8e0e7; border-radius: 8px; padding: 24px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; }}
    .button, button {{ background: #0b6efd; color: white; border: 0; border-radius: 6px; padding: 10px 14px; text-decoration: none; cursor: pointer; }}
    .danger {{ background: #b42318; }}
    .notice {{ background: #e9f7ef; border-left: 4px solid #1f8f4d; padding: 12px; margin: 16px 0; }}
    .error {{ background: #fdecec; border-left: 4px solid #b42318; padding: 12px; margin: 16px 0; }}
    label {{ display: block; margin-top: 12px; font-weight: bold; }}
    input {{ width: 100%; max-width: 420px; padding: 10px; margin-top: 6px; border: 1px solid #bdc7d0; border-radius: 6px; }}
    li {{ margin: 8px 0; }}
  </style>
</head>
<body>
  <header>
    <nav>
      <a href="/">Home</a>
      <a href="/dashboard">Dashboard</a>
      <a href="/login">Login</a>
      <a href="/logout">Logout</a>
    </nav>
  </header>
  <main>{body}</main>
</body>
</html>"""


def redirect(location, extra_headers=None):
    headers = [("Location", location)]
    if extra_headers:
        headers.extend(extra_headers)
    return 302, "", headers


class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/":
            self.render_home()
        elif parsed.path == "/login":
            message = "Please sign in to continue." if parse_qs(parsed.query).get("from") else ""
            self.render_login(message=message)
        elif parsed.path == "/dashboard":
            if not self.current_user():
                self.send_response_body(*redirect("/login?from=dashboard"))
                return
            self.render_dashboard()
        elif parsed.path == "/add-task":
            if not self.current_user():
                self.send_response_body(*redirect("/login?from=add-task"))
                return
            self.render_add_task()
        elif parsed.path == "/success":
            if not self.current_user():
                self.send_response_body(*redirect("/login?from=success"))
                return
            self.render_success()
        elif parsed.path == "/logout":
            self.send_response_body(*redirect("/", [("Set-Cookie", "sid=; Path=/; Max-Age=0")]))
        elif parsed.path == "/trigger-error":
            self.send_response_body(*page("Server Error", '<section class="panel"><h1>Server Error</h1><p class="error">Intentional demo failure.</p></section>', 500))
        else:
            self.send_response_body(*page("Not Found", '<section class="panel"><h1>Not Found</h1><p class="error">This route does not exist.</p></section>', 404))

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == "/login":
            self.handle_login()
        elif parsed.path == "/add-task":
            self.handle_add_task()
        elif parsed.path.startswith("/delete-task/"):
            self.handle_delete_task(parsed.path)
        else:
            self.send_response_body(*page("Not Found", '<section class="panel"><h1>Not Found</h1></section>', 404))

    def render_home(self):
        body = """
<section class="panel">
  <h1>Physical Flow Test Demo</h1>
  <p>A tiny web app for proving browser workflows with real execution artifacts.</p>
  <p><a class="button" href="/login" role="button">Get Started</a></p>
  <div class="grid">
    <div><h2>CTA</h2><p>Homepage to login.</p></div>
    <div><h2>Auth</h2><p>Fake login and dashboard guard.</p></div>
    <div><h2>Forms</h2><p>Success and failure states.</p></div>
  </div>
</section>"""
        self.send_response_body(*page("Home", body))

    def render_login(self, message="", error=""):
        notice = f'<p class="notice">{html.escape(message)}</p>' if message else ""
        error_html = f'<p class="error">{html.escape(error)}</p>' if error else ""
        body = f"""
<section class="panel">
  <h1>Sign in</h1>
  {notice}
  {error_html}
  <form method="post" action="/login">
    <label for="username">Username</label>
    <input id="username" name="username" autocomplete="username">
    <label for="password">Password</label>
    <input id="password" name="password" type="password" autocomplete="current-password">
    <p><button type="submit">Sign in</button></p>
  </form>
  <p>Use <code>test_user</code> / <code>test_pass</code>.</p>
</section>"""
        self.send_response_body(*page("Login", body))

    def render_dashboard(self):
        task_items = "\n".join(
            f'<li>{html.escape(task["title"])} '
            f'<form method="post" action="/delete-task/{task["id"]}" style="display:inline">'
            f'<button class="danger" type="submit">Delete</button></form></li>'
            for task in tasks
        )
        body = f"""
<section class="panel">
  <h1>Dashboard</h1>
  <p class="notice">Signed in as test_user.</p>
  <p><a class="button" href="/add-task">Add Task</a></p>
  <h2>Tasks</h2>
  <ul>{task_items}</ul>
</section>"""
        self.send_response_body(*page("Dashboard", body))

    def render_add_task(self, error=""):
        error_html = f'<p class="error">{html.escape(error)}</p>' if error else ""
        body = f"""
<section class="panel">
  <h1>Add Task</h1>
  {error_html}
  <form method="post" action="/add-task">
    <label for="title">Task title</label>
    <input id="title" name="title">
    <p><button type="submit">Create Task</button></p>
  </form>
</section>"""
        self.send_response_body(*page("Add Task", body))

    def render_success(self):
        body = """
<section class="panel">
  <h1>Task Created</h1>
  <p class="notice">The task was created successfully.</p>
  <p><a class="button" href="/dashboard">Back to Dashboard</a></p>
</section>"""
        self.send_response_body(*page("Success", body))

    def handle_login(self):
        data = self.read_form()
        if data.get("username", [""])[0] == TEST_USER and data.get("password", [""])[0] == TEST_PASS:
            sid = secrets.token_urlsafe(16)
            sessions[sid] = TEST_USER
            self.send_response_body(*redirect("/dashboard", [("Set-Cookie", f"sid={sid}; Path=/; HttpOnly; SameSite=Lax")]))
            return
        self.render_login(error="Invalid username or password.")

    def handle_add_task(self):
        global next_task_id
        if not self.current_user():
            self.send_response_body(*redirect("/login?from=add-task"))
            return
        data = self.read_form()
        title = data.get("title", [""])[0].strip()
        if not title:
            self.render_add_task(error="Task title is required.")
            return
        if "fail" in title.lower():
            self.render_add_task(error="Demo failure: task titles cannot contain 'fail'.")
            return
        tasks.append({"id": next_task_id, "title": title})
        next_task_id += 1
        self.send_response_body(*redirect("/success"))

    def handle_delete_task(self, path):
        if not self.current_user():
            self.send_response_body(*redirect("/login?from=delete-task"))
            return
        task_id = int(path.rsplit("/", 1)[-1])
        tasks[:] = [task for task in tasks if task["id"] != task_id]
        self.send_response_body(*redirect("/dashboard"))

    def current_user(self):
        raw_cookie = self.headers.get("Cookie", "")
        jar = cookies.SimpleCookie(raw_cookie)
        sid = jar.get("sid")
        if not sid:
            return None
        return sessions.get(sid.value)

    def read_form(self):
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length).decode("utf-8")
        return parse_qs(raw)

    def send_response_body(self, status, body, headers=None):
        encoded = body.encode("utf-8")
        self.send_response(status)
        for name, value in headers or []:
            self.send_header(name, value)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), DemoHandler)
    print(f"Physical Flow Demo running at http://{HOST}:{PORT}")
    server.serve_forever()
