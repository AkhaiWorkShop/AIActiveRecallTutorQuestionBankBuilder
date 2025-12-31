import re
from collections import OrderedDict

QUESTION_NO_REGEX = re.compile(r'(?<!\w)(\d{1,2})[\.\)]\s+')

def build_question_blocks(text):
    matches = list(QUESTION_NO_REGEX.finditer(text))
    blocks = {}

    for i, m in enumerate(matches):
        q_no = int(m.group(1))
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        blocks[q_no] = text[start:end].strip()

    return blocks