from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def load_logs(file_path):
    with open(file_path, "r") as f:
        return f.read()

def create_vector_db(text):
    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_texts(chunks, embeddings)
    db.save_local("vector_db")

    print("✅ Vector DB created successfully!")

if __name__ == "__main__":
    logs = load_logs("data/sample_logs.txt")
    create_vector_db(logs)