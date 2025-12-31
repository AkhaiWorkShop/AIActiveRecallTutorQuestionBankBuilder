import json, os


PATH = "logs/synonym_suggestions.json"


def load_store():
    if not os.path.exists(PATH):
        return {}
    with open(PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_store(data: dict):
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
with open(PATH, "w", encoding="utf-8") as f:
json.dump(data, f, ensure_ascii=False, indent=2)