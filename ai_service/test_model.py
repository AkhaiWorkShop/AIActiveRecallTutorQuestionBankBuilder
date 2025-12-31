from sentence_transformers import SentenceTransformer
import time

print("Starting model load...")
start = time.time()
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
end = time.time()
print(f"Model loaded in {end - start:.2f} seconds")

text = "Halo dunia"
embedding = model.encode(text)
print(f"Embedding shape: {embedding.shape}")
print("Test successful!")
