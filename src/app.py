import os
import requests
from dotenv import load_dotenv
from retriever import retrieve

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY not found in .env")

def query_llm(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "nvidia/nemotron-3-super-120b-a12b:free",  # ✅ FIXED
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "reasoning": {"enabled": True}  # ✅ enables reasoning
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"❌ Error: {response.text}"

    result = response.json()
    message = result["choices"][0]["message"]

    return message.get("content", "No response generated")
def ask_question(query):
    context = retrieve(query)

    prompt = f"""
You are a Kubernetes expert.

Analyze the logs below and answer clearly.

Context:
{context}

Question:
{query}

Provide:
- Root Cause
- Evidence
- Fix
- Commands
"""

    return query_llm(prompt)


if __name__ == "__main__":
    print("☸️ Kubernetes RAG Assistant Started")

    while True:
        query = input("\nAsk your question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        response = ask_question(query)
        print("\n🤖 Response:\n", response)