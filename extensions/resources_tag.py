import re
from markdown.extensions import Extension as MDXExtension
from markdown.preprocessors import Preprocessor as MDXPreprocessor


class ResourcesTagExtension(MDXExtension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(ResourcesTagPreprocessor(), "resources_table", 175)


class ResourcesTagPreprocessor(MDXPreprocessor):
    tag = re.compile(r"!resources\s*\[(.+)\]")

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = self.tag.search(line)
            if match:
                raw_triples = match.group(1).strip()
                triples = self.parse_triples(raw_triples)
                html = self.build_table(triples)
                if html is not None:
                    new_lines.append(html)
            else:
                new_lines.append(line)
        return new_lines

    def parse_triples(self, raw_triples: str):
        triples = []
        for item in re.findall(r"\(([^,]+?),\s*([^,]+?),\s*([^)]+?)\)", raw_triples):
            title, link, source = item
            triples.append((title.strip(), link.strip(), source.strip()))
        return triples

    def build_table(self, triples) -> str | None:
        if not triples:
            return None
        rows = []
        for title, link, source in triples:
            title_cell = f'<a href="{link}" target="_blank" rel="noopener noreferrer">{title}</a>'
            rows.append(f"| {source} | {title_cell} |")

        table = "| Source | Resources |\n|-|-|\n"
        table += "\n".join(rows)
        return table


def makeExtension(**kwargs):
    return ResourcesTagExtension(**kwargs)
