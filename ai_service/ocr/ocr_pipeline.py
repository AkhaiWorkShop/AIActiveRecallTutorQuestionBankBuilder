from ocr.ocr_engine import run_ocr
from ocr.confidence import compute_confidence

def ocr_with_retry(file, lang="ind", max_retry=2):
    results = []
    last_output = None

    for attempt in range(max_retry + 1):
        result = run_ocr(
            file,
            lang=lang,
            attempt=attempt  # ← penting
        )

        raw = result["ocr"]["raw_text"]
        clean = result["ocr"].get("clean_text", "")
        ocr_conf = result["meta"]["avg_confidence"]
        parsed = result["questions"]

        confidences = [
            compute_confidence(ocr_conf, q["question_text"], q["options"])
            for q in parsed
        ]

        last_output = (parsed, confidences)

        if not should_retry(confidences):
            break

    return last_output
