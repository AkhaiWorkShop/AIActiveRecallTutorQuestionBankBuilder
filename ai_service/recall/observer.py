import json
import os
from datetime import datetime

LOG_PATH = "logs/evaluations.jsonl"

def log_evaluation(payload: dict):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    payload["timestamp"] = datetime.utcnow().isoformat()
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")