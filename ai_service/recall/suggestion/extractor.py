import re
STOPWORDS = {"yang", "dan", "itu", "adalah", "ialah", "atau", "dari", "ke", "di"}
def extract_candidates(text: str):
    tokens = re.findall(r"\b[a-z]{4,}\b", text.lower())
    return list(set(t for t in tokens if t not in STOPWORDS))