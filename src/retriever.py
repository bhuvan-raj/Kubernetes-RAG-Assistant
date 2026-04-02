from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def load_db():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local("vector_db", embeddings)

def retrieve(query):
    db = load_db()
    docs = db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])