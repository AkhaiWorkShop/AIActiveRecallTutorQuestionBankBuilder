def aggregate(store: dict, suggestion: dict):
    key = f"{suggestion['term']}|{suggestion['concept']}"
    if key not in store:
        store[key] = {"count": 1, "avg_similarity": suggestion["similarity"]}
    else:
        item = store[key]
        total = item["avg_similarity"] * item["count"]
        item["count"] += 1
        item["avg_similarity"] = round((total + suggestion["similarity"]) / item["count"], 3)
    return store