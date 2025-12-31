from sentence_transformers import SentenceTransformer
_model = None
def _load_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    return _model

def embed(text: str):
    model = _load_model()
    return model.encode(text)