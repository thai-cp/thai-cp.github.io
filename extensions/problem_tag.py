import re
import yaml
from pathlib import Path
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

class Extension(Extension):
    def __init__(self, problems_dir="docs/problems", **kwargs):
        self.problems_dir = Path(problems_dir)
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(
            Preprocessor(self.problems_dir), 'problem_table', 175
        )

class Preprocessor(Preprocessor):
    tag = re.compile(r"!problems\s*\[([^\]]+)\]")

    def __init__(self, problems_dir):
        super().__init__()
        self.problems_dir = problems_dir

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = self.tag.search(line)
            if match:
                problem_ids = [p.strip() for p in match.group(1).split(",")]
                html = self.build_table(problem_ids)
                new_lines.append(html)
            else:
                new_lines.append(line)
        return new_lines

    def build_table(self, problem_ids):
        rows = []
        for pid in problem_ids:
            file_path = self.problems_dir / f"{pid}.md"

            title, source, difficulty, link = pid, None, "?", None

            if file_path.exists():
                with open(file_path, encoding="utf-8") as f:
                    lines = f.readlines()

                if lines and lines[0].strip() == "---":
                    meta_lines = []
                    for line in lines[1:]:
                        if line.strip() == "---":
                            break
                        meta_lines.append(line)
                    meta = yaml.safe_load("".join(meta_lines)) or {}

                    title = meta.get("title", pid)
                    if (title == None): title = pid
                    source = meta.get("source")
                    difficulty = meta.get("difficulty", "?")
                    if (difficulty == None): difficulty = '?'
                    link = meta.get("link")

            problem_cell = f"<a href=\"{link}\" target=\"_blank\" rel=\"noopener noreferrer\">{title}</a>" if link else title
            solution_cell = f"<a href=\"/problems/{pid}\" target=\"_blank\" rel=\"noopener noreferrer\">View</a>"

            rows.append(f"| {problem_cell} | {source} | {difficulty} | {solution_cell} |")

        table = "| Problem | Source | Difficulty | Solution |\n|-|-|-|-|\n"
        table += "\n".join(rows)
        return table

def makeExtension(**kwargs):
    return Extension(**kwargs)
