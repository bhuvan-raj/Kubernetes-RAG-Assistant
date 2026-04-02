import streamlit as st
from app import ask_question

st.title("☸️ Kubernetes RAG Assistant")

query = st.text_input("Ask a Kubernetes question:")

if query:
    response = ask_question(query)
    st.write(response)