from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Sample documents – replace with your NCERT content
documents = [
    "Photosynthesis is the process by which green plants prepare food using sunlight.",
    "The circulatory system consists of the heart, blood vessels, and blood.",
    "Newton's laws of motion describe the relationship between force and motion.",
]

# Step 1: Load embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Step 2: Convert to embeddings
embeddings = embedder.encode(documents, convert_to_numpy=True)

# Step 3: Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Step 4: Save the index and documents
faiss.write_index(index, "faiss_index.bin")
with open("docs.pkl", "wb") as f:
    pickle.dump(documents, f)

print("✅ FAISS index and documents saved successfully!")
