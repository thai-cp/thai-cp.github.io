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
        md.preprocessors.register(
            Preprocessor(), 'unfinished_tag', 175
        )

class Preprocessor(Preprocessor):
    tag = re.compile(r"!unfinished")

    def __init__(self):
        super().__init__()

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = self.tag.search(line)
            if match:
                html = self.build_tag()
                new_lines.append(html)
            else:
                new_lines.append(line)
        return new_lines

    def build_tag(self):
        rows = []
        rows.append('!!! failure "บทเรียนนี้ยังไม่สมบูรณ์"')
        rows.append('    หากใครต้องการช่วยเหลือ สามารถส่ง Pull Request มาได้ทาง <a href=\"https://github.com/thai-cp/thai-cp.github.io\" target=\"_blank\" rel=\"noopener noreferrer\">GitHub</a>')
        return "\n".join(rows)

def makeExtension(**kwargs):
    return Extension(**kwargs)
