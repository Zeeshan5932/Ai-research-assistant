from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

VECTOR_PATH = "data/vector_store"

def get_vector_store(documents=None):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    if os.path.exists(VECTOR_PATH) and documents is None:
        return FAISS.load_local(VECTOR_PATH, embeddings)

    db = FAISS.from_documents(documents, embeddings)
    db.save_local(VECTOR_PATH)
    return db
