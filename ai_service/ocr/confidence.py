import re

def compute_confidence(
    ocr_conf: float,
    question: str,
    choices: list
) -> float:
    score = 0.0

    # OCR weight
    score += ocr_conf * 0.4

    # Structure confidence
    if choices:
        if len(choices) >= 4:
            score += 0.4
        if [c["label"] for c in choices] == ["A", "B", "C", "D"]:
            score += 0.2
    else:
        if len(question) > 20:
            score += 0.4
        if question.endswith("?") or question.endswith("!"):
            score += 0.2

    # Noise penalty
    noise = len(re.findall(r'[�#]', question))
    score -= min(noise * 0.05, 0.3)

    return round(max(0.0, min(score, 1.0)), 2)
