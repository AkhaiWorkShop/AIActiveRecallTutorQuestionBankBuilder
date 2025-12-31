import numpy as np
def cosine_similarity(v1, v2) -> float:
    if v1 is None or v2 is None:
        return 0.0
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))