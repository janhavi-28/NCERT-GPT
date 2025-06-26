import streamlit as st
from app import answer_query

st.title("📘 NCERT Chatbot (Class 10 - Biology)")
query = st.text_input("Ask a question from the textbook")

if query:
    with st.spinner("Answering..."):
        result = answer_query(query)
        st.write(result)
