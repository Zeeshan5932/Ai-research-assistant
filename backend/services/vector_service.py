from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os

VECTOR_PATH = "data/vector_store"

def get_vector_store(documents=None):
    embeddings = OpenAIEmbeddings()

    if os.path.exists(VECTOR_PATH) and documents is None:
        return FAISS.load_local(VECTOR_PATH, embeddings)

    db = FAISS.from_documents(documents, embeddings)
    db.save_local(VECTOR_PATH)
    return db
