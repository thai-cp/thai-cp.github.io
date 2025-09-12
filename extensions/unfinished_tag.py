import re
from markdown.extensions import Extension as MDXExtension
from markdown.preprocessors import Preprocessor as MDXPreprocessor


class UnfinishedTagExtension(MDXExtension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(UnfinishedTagPreprocessor(), "unfinished_tag", 175)


class UnfinishedTagPreprocessor(MDXPreprocessor):
    tag = re.compile(r"!unfinished")

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = self.tag.search(line)
            if match:
                html = self.build_tag()
                if html:
                    new_lines.append(html)
            else:
                new_lines.append(line)
        return new_lines

    def build_tag(self):
        return (
            '!!! failure "บทเรียนนี้ยังไม่สมบูรณ์"\n'
            '    หากใครต้องการช่วยเหลือ สามารถส่ง Pull Request มาได้ทาง <a href="https://github.com/thai-cp/thai-cp.github.io" target="_blank" rel="noopener noreferrer">GitHub</a>'
        )


def makeExtension(**kwargs):
    return UnfinishedTagExtension(**kwargs)
