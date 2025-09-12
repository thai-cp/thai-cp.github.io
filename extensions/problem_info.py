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
        md.preprocessors.register(Preprocessor(self.problems_dir), "problem_info", 175)


class Preprocessor(Preprocessor):
    tag = re.compile(r"!problem_info\s+(\S+)")

    def __init__(self, problems_dir):
        super().__init__()
        self.problems_dir = problems_dir

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = self.tag.search(line)
            if match:
                problem_id = match.group(1).strip()
                html = self.build_info(problem_id)
                new_lines.append(html)
            else:
                new_lines.append(line)
        return new_lines

    def build_info(self, pid):
        rows = []
        file_path = self.problems_dir / f"{pid}.md"

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

                source = meta.get("source")
                difficulty = meta.get("difficulty", "?")
                if difficulty is None:
                    difficulty = "?"
                link = meta.get("link")
                extsol = meta.get("extsol", None)
                fsource = meta.get("fsource", None)
                source = meta.get("fsource", None)
                tags = meta.get("tags", None)
                prereq = meta.get("prereq", None)

            rows.append('!!! note ""')
            rows.append(
                f'    <a href="{link}" target="_blank" rel="noopener noreferrer">**View Problem Statement** :material-open-in-new:</a>\n'
            )
            rows.append(f"    **Source**: {fsource if fsource else source}\n")
            if difficulty:
                rows.append(f"    **Difficulty**: {difficulty}\n")
            if tags:
                rows.append(f"    **Tags**: {', '.join(tags)}\n")
            if prereq:
                rows.append(
                    f"    **Prerequisites**:\n\n"
                    + "".join(f"    - {p}\n" for p in prereq)
                )
            if extsol:
                rows.append(
                    f'    <a href="{extsol}" target="_blank" rel="noopener noreferrer">**View External Solution** :material-open-in-new:</a>\n'
                )

            return "\n".join(rows)


def makeExtension(**kwargs):
    return Extension(**kwargs)
