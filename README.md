# 📚 NCERT-GPT

> A RAG-powered Q&A chatbot for NCERT Class 9 Science — ask questions, get source-grounded answers instantly.

---

## 🧠 What is NCERT-GPT?

NCERT-GPT is a lightweight **Retrieval-Augmented Generation (RAG)** chatbot built with a quantized LLaMA 3 model (Q4_K_M via `llama.cpp`). It answers both general knowledge questions and NCERT textbook-specific queries using semantic search over indexed document chunks.

---

## ✨ Features

- 🔍 **RAG Pipeline** — FAISS vector store + Sentence Transformer embeddings for semantic retrieval
- 📖 **NCERT-aware** — indexed over Class 9 Science textbook content
- 💬 **Interactive Chat UI** — built with Streamlit, displays full chat history
- ⚡ **Offline Capable** — runs locally using quantized GGUF model via `llama-cpp-python`
- 🎯 **Source-grounded answers** — reduces hallucinations by retrieving relevant chunks before generating

---

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| LLM | LLaMA 3 (Q4_K_M quantized, GGUF) |
| Inference | llama-cpp-python |
| Vector Store | FAISS |
| Embeddings | Sentence Transformers |
| UI | Streamlit |
| Preprocessing | Custom pipeline (preprocess.py + build_index.py) |

---

## 📁 Project Structure

```
NCERT-GPT/
├── app.py               # Main Streamlit chatbot app
├── streamlit_app.py     # Alternate Streamlit entry point
├── preprocess.py        # Text extraction and chunking
├── build_index.py       # Embedding generation + FAISS index builder
├── class9_science.txt   # NCERT textbook source content
├── faiss_index.bin      # Prebuilt FAISS vector index
├── chunks.pkl           # Serialized text chunks
├── docs.pkl             # Serialized document store
└── requirements.txt     # All dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/janhavi-28/NCERT-GPT.git
cd NCERT-GPT
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 💬 Sample Questions You Can Ask

**NCERT-based**
- What is Ohm's Law?
- Explain Mendel's laws of inheritance.
- What are the properties of matter?

**General Knowledge**
- Explain Newton's Laws of Motion.
- What is the difference between mitosis and meiosis?

**Reasoning**
- Solve 23 × 42
- Write a Python function to check if a number is prime.

---

## 🙏 Acknowledgements

- [Meta AI](https://ai.meta.com) for LLaMA 3
- [Hugging Face](https://huggingface.co) for model hosting
- [llama.cpp](https://github.com/ggerganov/llama.cpp) for fast local inference
- [FAISS](https://github.com/facebookresearch/faiss) for vector similarity search

---

## 👩‍💻 Author

**Janhavi Kolekar** — [LinkedIn](https://www.linkedin.com/in/janhavi-kolekar-0b5a30246) | [GitHub](https://github.com/janhavi-28)
