def should_retry(confidences: list, threshold=0.6) -> bool:
    avg = sum(confidences) / len(confidences)
    return avg < threshold
