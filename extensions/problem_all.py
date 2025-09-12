import re
import yaml
import os
from pathlib import Path
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class Extension(Extension):
    def __init__(self, problems_dir="docs/problems", **kwargs):
        self.problems_dir = Path(problems_dir)
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(Preprocessor(self.problems_dir), "problem_all", 175)


class Preprocessor(Preprocessor):
    tag = re.compile(r"!problem_all")

    def __init__(self, problems_dir):
        super().__init__()
        self.problems_dir = problems_dir

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = self.tag.search(line)
            if match:
                html = self.build_card()
                new_lines.append(html)
            else:
                new_lines.append(line)
        return new_lines

    def build_card(self):
        rows = []

        def sort_key(s: str):
            return [
                int(text) if text.isdigit() else text.lower()
                for text in re.split(r"(\d+)", s)
            ]

        problems = []
        for f in os.listdir(self.problems_dir):
            if not f.endswith(".md"):
                continue
            pid, _ = os.path.splitext(f)
            if pid == "index":
                continue

            file_path = self.problems_dir / f"{pid}.md"
            title, source, difficulty, link = pid, None, "?", None

            if file_path.exists():
                try:
                    with open(file_path, encoding="utf-8") as fobj:
                        lines = fobj.readlines()
                except OSError:
                    lines = []

                if lines and lines[0].strip() == "---":
                    meta_lines = []
                    for line in lines[1:]:
                        if line.strip() == "---":
                            break
                        meta_lines.append(line)
                    try:
                        meta = yaml.safe_load("".join(meta_lines)) or {}
                    except yaml.YAMLError:
                        meta = {}

                    title = meta.get("title", pid) or pid
                    source = meta.get("source")
                    difficulty = meta.get("difficulty", "?") or "?"
                    link = meta.get("link")

            problems.append(
                {
                    "pid": pid,
                    "title": title,
                    "source": source,
                    "difficulty": difficulty,
                    "link": link,
                }
            )

        problems.sort(key=lambda x: sort_key(x["pid"]))

        for p in problems:
            pid = p["pid"]
            title = p["title"]
            source = p["source"]
            difficulty = p["difficulty"]
            link = p["link"]
            rows.append(
                f'-   <a href="{link}" target="_blank" rel="noopener noreferrer">**{title}**</a>'
                if link
                else title
            )
            rows.append("    ---")
            rows.append(f"    **Source**: {source}")
            rows.append(f"    **Difficulty**: {difficulty}")
            rows.append(
                f'    <a href="/problems/{pid}" target="_blank" rel="noopener noreferrer">**View Solution** :material-open-in-new:</a>'
            )

        table = '<div class="grid cards" markdown>'
        table += "\n\n".join(rows)
        table += "\n\n</div>"
        return table


def makeExtension(**kwargs):
    return Extension(**kwargs)
