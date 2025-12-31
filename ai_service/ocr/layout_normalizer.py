import re
from typing import List


QUESTION_NUMBER_REGEX = re.compile(r'^\s*(\d{1,2})[\.\)]')


def split_lines(text: str) -> List[str]:
    return [l.strip() for l in text.splitlines() if l.strip()]

def normalize_two_column_text(text: str) -> str:
    """
    Force linear reading by reordering detected question numbers.
    """
    lines = text.splitlines()
    buffer = []

    for line in lines:
        if line.strip():
            buffer.append(line.strip())

    return "\n".join(buffer)



def detect_columns(lines: List[str]):
    """
    Heuristik:
    - baris panjang → kemungkinan gabungan kiri+kanan
    - kita split tengah
    """
    left, right = [], []

    for line in lines:
        if len(line) > 80:
            mid = len(line) // 2
            left.append(line[:mid].strip())
            right.append(line[mid:].strip())
        else:
            left.append(line)

    return left, right


def reorder_by_question_number(left: List[str], right: List[str]) -> str:
    """
    Gabungkan berdasarkan pola:
    1 kiri, 2 kanan, 3 kiri, 4 kanan, dst
    """
    ordered = []
    li = ri = 0

    expected = 1
    max_iter = len(left) + len(right)

    for _ in range(max_iter):
        # cek kiri
        if li < len(left):
            m = QUESTION_NUMBER_REGEX.match(left[li])
            if m and int(m.group(1)) == expected:
                ordered.append(left[li])
                li += 1
                expected += 1
                continue

        # cek kanan
        if ri < len(right):
            m = QUESTION_NUMBER_REGEX.match(right[ri])
            if m and int(m.group(1)) == expected:
                ordered.append(right[ri])
                ri += 1
                expected += 1
                continue

        # fallback: maju kiri dulu
        if li < len(left):
            ordered.append(left[li])
            li += 1
        elif ri < len(right):
            ordered.append(right[ri])
            ri += 1
        else:
            break

    return "\n".join(ordered)


def normalize_layout(text: str) -> str:
    lines = split_lines(text)
    left, right = detect_columns(lines)
    return reorder_by_question_number(left, right)
