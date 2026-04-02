
# ☸️ Kubernetes RAG Assistant

A Retrieval-Augmented Generation (RAG) based intelligent assistant designed to analyze Kubernetes issues and provide root cause analysis, fixes, and commands using real-world context.

---

## 🚀 Project Overview

This project combines:

- 🔍 **Vector Search (FAISS)** for retrieving relevant Kubernetes knowledge
- 🤖 **LLM (via OpenRouter)** for intelligent reasoning
- ☸️ **Kubernetes-focused prompts** for SRE-style debugging

It allows users to ask questions like:

> "Why is my pod in CrashLoopBackOff?"

And get structured answers with:
- Root Cause
- Evidence
- Fix
- Commands

---

## 🧠 LLM Used

This project uses:

- **Model:** `nvidia/nemotron-3-super-120b-a12b:free`  
- **Provider:** OpenRouter  
- **Capabilities:**
  - Reasoning-enabled responses
  - Multi-step analysis
  - High-quality structured output

---

## 🏗️ Architecture

```

User Query
↓
Retriever (FAISS Vector DB)
↓
Relevant Context
↓
LLM (OpenRouter - Nemotron 120B)
↓
Structured Kubernetes Answer

```

---

## 📁 Project Structure

```

rag-assistant/
│
├── src/
│   ├── app.py            # Main application (CLI)
│   ├── ingestion.py      # Data ingestion & vector DB creation
│   ├── retriever.py      # FAISS-based retrieval logic
│   ├── k8s_fetcher.py    # (Planned) Fetch real Kubernetes logs
│   └── ui.py             # (Optional UI placeholder)
│
├── data/                 # Kubernetes docs / logs
├── vector_db/            # FAISS index storage
├── venv/                 # Virtual environment
│
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd rag-assistant
````

---

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

### 5. Ingest Data

```bash
python src/ingestion.py
```

---

### 6. Run the Application

```bash
python src/app.py
```

---

## 🧪 Example Usage

```
Ask your question: pod is in CrashLoopBackOff
```

### ✅ Output:

```
🔍 Root Cause:
...

📊 Evidence:
...

🛠 Fix:
...

💻 Commands:
kubectl logs <pod>
kubectl describe pod <pod>
```

---

## 🔧 Technologies Used

* Python
* FAISS (Vector DB)
* LangChain (Retriever)
* Sentence Transformers (Embeddings)
* OpenRouter API
* NVIDIA Nemotron 120B (LLM)

---

## ⚠️ Known Warnings

* HuggingFace token warning → optional
* `embeddings.position_ids` → safe to ignore

---

 

---

## 📜 License

MIT License

````

---

