import faiss
import numpy as np

class VectorStore:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)

    def add_embeddings(self, embeddings):
        embeddings = np.array(embeddings).astype('float32')

        self.index.add(embeddings)

    def search(self, query_embedding, top_k=3):
        query_embedding = np.array([query_embedding]).astype('float32')

        distances, indices = self.index.search(query_embedding, top_k)

        return distances, indices

    def save(self, path):
        faiss.write_index(self.index, path)

    def load(self, path):
        self.index = faiss.read_index(path)