import csv
from pathlib import Path

SLANG_MAP = {}

def load_slang(path=None):
    global SLANG_MAP
    if path is None:
        path = Path(__file__).parent.parent / "data" / "indo_slang_new.csv"
    
    with open(path, encoding="utf-8", errors="replace") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2:
                slang, formal = row[0].strip(), row[1].strip()
                SLANG_MAP[slang] = formal


def normalize_slang(text: str) -> str:
    if not SLANG_MAP:
        load_slang()
    tokens = text.split()
    normalized = [SLANG_MAP.get(t, t) for t in tokens]
    return " ".join(normalized)
