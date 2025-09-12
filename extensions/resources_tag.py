import re
import yaml
from pathlib import Path
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class Extension(Extension):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(Preprocessor(), "resources_table", 175)


class Preprocessor(Preprocessor):
    tag = re.compile(r"!resources\s*\[(.+)\]")

    def __init__(self):
        super().__init__()

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = self.tag.search(line)
            if match:
                raw_triples = match.group(1).strip()
                triples = self.parse_triples(raw_triples)
                html = self.build_table(triples)
                new_lines.append(html)
            else:
                new_lines.append(line)
        return new_lines

    def parse_triples(self, raw_triples):
        triples = []
        for item in re.findall(r"\(([^,]+?),\s*([^,]+?),\s*([^)]+?)\)", raw_triples):
            title, link, source = item
            triples.append((title.strip(), link.strip(), source.strip()))
        return triples

    def build_table(self, triples):
        rows = []
        for title, link, source in triples:
            title_cell = f'<a href="{link}" target="_blank" rel="noopener noreferrer">{title}</a>'
            rows.append(f"| {source} | {title_cell} |")

        table = "| Source | Resources |\n|-|-|\n"
        table += "\n".join(rows)
        return table


def makeExtension(**kwargs):
    return Extension(**kwargs)
