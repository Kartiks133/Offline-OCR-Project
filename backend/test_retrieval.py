import json
import os

from retrieval.generate_answer import generate_answer
from retrieval.chunker import chunk_text
from retrieval.embedder import generate_embeddings
from retrieval.embedder import model
from retrieval.vector_store import VectorStore


# PATH TO JSON FILE
json_folder = "extracted_text"

json_files = os.listdir(json_folder)

if not json_files:
    print("No extracted text found.")
    exit()

# GET LATEST JSON FILE
latest_json = os.path.join(
    json_folder,
    json_files[-1]
)

# LOAD JSON
with open(latest_json, "r", encoding="utf-8") as f:
    data = json.load(f)

# COMBINE ALL PAGE TEXT
full_text = ""

for page in data["pages"]:
    full_text += page["text"] + "\n"

# CHUNK TEXT
chunks = chunk_text(full_text)

print(f"\nTotal Chunks: {len(chunks)}")

# CREATE EMBEDDINGS
embeddings = generate_embeddings(chunks)

# CREATE VECTOR STORE
dimension = embeddings.shape[1]

store = VectorStore(dimension)

store.add_embeddings(embeddings)

print("Embeddings stored successfully.")

# ASK QUESTION
query = input("\nAsk a question: ")

# CONVERT QUESTION TO EMBEDDING
query_embedding = model.encode(query)

# SEARCH RELEVANT CHUNKS
distances, indices = store.search(query_embedding)

# BUILD CONTEXT
context = ""

for idx in indices[0]:
    context += chunks[idx] + "\n"

# GENERATE AI ANSWER
answer = generate_answer(
    query,
    context
)

# PRINT FINAL ANSWER
print("\nAI ANSWER:\n")

print(answer)