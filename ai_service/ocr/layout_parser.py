import re
from typing import List, Dict

CHOICE_REGEX = re.compile(
    r'(?P<label>[A-Da-d])[\.\)]\s*(?P<text>.+)',
    re.MULTILINE
)

QUESTION_SPLIT_REGEX = re.compile(
    r'(^|\n)(\d+)[\.\)]\s+',
    re.MULTILINE
)

def split_question_blocks(text: str) -> List[str]:
    """
    Split OCR text into question blocks using numbering.
    """
    indices = [m.start() for m in QUESTION_SPLIT_REGEX.finditer(text)]

    if not indices:
        return [text.strip()]

    blocks = []
    for i in range(len(indices)):
        start = indices[i]
        end = indices[i + 1] if i + 1 < len(indices) else len(text)
        blocks.append(text[start:end].strip())

    return blocks


def parse_multiple_choice(block: str) -> Dict:
    choices = []

    for match in CHOICE_REGEX.finditer(block):
        label = match.group("label").upper()
        text = match.group("text").strip()
        choices.append({"label": label, "text": text})

    question_text = CHOICE_REGEX.split(block)[0]
    question_text = QUESTION_SPLIT_REGEX.sub("", question_text).strip()

    return {
        "type": "MULTIPLE_CHOICE",
        "question": question_text,
        "choices": choices
    }


def parse_essay(block: str) -> Dict:
    question_text = QUESTION_SPLIT_REGEX.sub("", block).strip()

    return {
        "type": "ESSAY",
        "question": question_text,
        "choices": []
    }


def parse_ocr_text(text: str) -> List[Dict]:
    """
    Main entry point: OCR clean_text → structured questions
    """
    blocks = split_question_blocks(text)
    results = []

    for block in blocks:
        mc = parse_multiple_choice(block)

        if len(mc["choices"]) >= 2:
            results.append({
                "raw_block": block,
                **mc
            })
        else:
            results.append({
                "raw_block": block,
                **parse_essay(block)
            })

    return results

def parse_question_block(q_no, block_text):
    choices = extract_choices(block_text)

    if len(choices) >= 3 and len(choices) <= 5:
        return {
            "question_no": q_no,
            "type": "MULTIPLE_CHOICE",
            "question": extract_question_text(block_text),
            "choices": choices
        }

    return {
        "question_no": q_no,
        "type": "ESSAY",
        "question": extract_question_text(block_text),
        "choices": []
    }