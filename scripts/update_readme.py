"""Refresh the "Recently shipped" section of README.md from my latest public commits.

Run by .github/workflows/update-readme.yml once a day. Set GITHUB_TOKEN to avoid
the unauthenticated rate limit; it works without one for occasional local runs.
"""

import json
import os
import re
import urllib.request
from datetime import datetime
from pathlib import Path

USER = "blessondavis"
README = Path(__file__).resolve().parent.parent / "README.md"
MAX_REPOS = 6
MAX_COMMITS = 5
MARKER = re.compile(r"(<!-- recent_commits starts -->\n).*?(<!-- recent_commits ends -->)", re.S)


def get(path):
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", "application/vnd.github+json")
    if token := os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def recent_commits():
    repos = get(f"/users/{USER}/repos?type=owner&sort=pushed&per_page=30")
    repos = [r for r in repos if not r["fork"] and r["name"] != USER][:MAX_REPOS]
    commits = []
    for repo in repos:
        for c in get(f"/repos/{USER}/{repo['name']}/commits?per_page={MAX_COMMITS}"):
            message = c["commit"]["message"].splitlines()[0].strip()
            if message.lower().startswith("merge"):
                continue
            commits.append({
                "repo": repo["name"],
                "message": message,
                "url": c["html_url"],
                "date": c["commit"]["author"]["date"],
            })
    commits.sort(key=lambda c: c["date"], reverse=True)
    return commits[:MAX_COMMITS]


def render(commits):
    lines = []
    for c in commits:
        day = datetime.fromisoformat(c["date"].replace("Z", "+00:00")).strftime("%d %b %Y")
        repo = f"[{c['repo']}](https://github.com/{USER}/{c['repo']})"
        lines.append(f"- [{c['message']}]({c['url']}) · {repo} · <sub>{day}</sub>")
    return "\n".join(lines) + "\n"


def main():
    text = README.read_text(encoding="utf-8")
    updated = MARKER.sub(lambda m: m.group(1) + render(recent_commits()) + m.group(2), text)
    if updated != text:
        README.write_text(updated, encoding="utf-8", newline="\n")
        print("README updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()
