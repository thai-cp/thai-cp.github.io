import re
import yaml
from pathlib import Path
from markdown.extensions import Extension as MDXExtension
from markdown.preprocessors import Preprocessor as MDXPreprocessor


class ProblemInfoExtension(MDXExtension):
    def __init__(self, problems_dir="docs/problems", **kwargs):
        self.problems_dir = Path(problems_dir)
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(
            ProblemInfoPreprocessor(self.problems_dir), "problem_info", 175
        )


class ProblemInfoPreprocessor(MDXPreprocessor):
    tag = re.compile(r"!problem_info\s+(\S+)")

    def __init__(self, problems_dir: Path):
        super().__init__()
        self.problems_dir = problems_dir

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = self.tag.search(line)
            if match:
                problem_id = match.group(1).strip()
                html = self.build_info(problem_id)
                if html is not None:
                    new_lines.append(html)
            else:
                new_lines.append(line)
        return new_lines

    def build_info(self, pid: str):
        rows = []
        file_path = self.problems_dir / f"{pid}.md"

        if not file_path.exists():
            return None

        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()

        if not (lines and lines[0].strip() == "---"):
            return None

        meta_lines = []
        for line in lines[1:]:
            if line.strip() == "---":
                break
            meta_lines.append(line)
        try:
            meta = yaml.safe_load("".join(meta_lines)) or {}
        except yaml.YAMLError:
            meta = {}

        source = meta.get("source")
        difficulty = meta.get("difficulty", "?") or "?"
        link = meta.get("link")
        extsol = meta.get("extsol")
        fsource = meta.get("fsource")
        source_display = fsource if fsource else source
        tags = meta.get("tags")
        prereq = meta.get("prereq")

        rows.append('!!! note ""')
        if link:
            rows.append(
                f'    <a href="{link}" target="_blank" rel="noopener noreferrer">**View Problem Statement** :material-open-in-new:</a>\n'
            )
        if source_display:
            rows.append(f"    **Source**: {source_display}\n")
        if difficulty:
            rows.append(f"    **Difficulty**: {difficulty}\n")
        if tags:
            rows.append(f"    **Tags**: {', '.join(tags)}\n")
        if prereq:
            rows.append(
                "    **Prerequisites**:\n\n" + "".join(f"    - {p}\n" for p in prereq)
            )
        if extsol:
            rows.append(
                f'    <a href="{extsol}" target="_blank" rel="noopener noreferrer">**View External Solution** :material-open-in-new:</a>\n'
            )

        return "\n".join(rows)


def makeExtension(**kwargs):
    return ProblemInfoExtension(**kwargs)
