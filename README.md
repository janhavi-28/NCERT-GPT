NCERT-GPT 

NCERT-GPT is a lightweight RAG (Retrieval-Augmented Generation) chatbot built using `llama.cpp` and a quantized version of LLaMA 3 (Q4_K_M). It is designed to answer both general knowledge and NCERT textbook-based questions.

Features

- Loads a local quantized GGUF model using `llama-cpp-python`
- Offline capable
- Displays chat history interactively
- Streams responses in a user-friendly UI with Streamlit
- Integrates with your NCERT documents via FAISS and RAG (optional)

Folder Structure


app.py                  # Main Streamlit chatbot app
preprocess.py           # Text extraction from PDF/notes
build_index.py          # Embedding + FAISS index builder
docs/                   # Contains textbook `.txt` files
embeddings/             # Numpy embedding files
models/                 # GGUF model file
faiss_index.bin         # FAISS vector index
requirements.txt        # All required dependencies


Run the App

1. Install dependencies
bash
pip install -r requirements.txt

2. Start the Streamlit app
bash
streamlit run app.py


Sample Questions

General Knowledge
- Who is the Prime Minister of India?
- Explain Newton's Laws of Motion.

NCERT-based (with RAG)
- What is Ohm's Law from Class 10 notes?
- Explain Mendel's laws of inheritance.

Reasoning/Code
- Solve 23 * 42
- Write a Python function to check prime
Acknowledgements

- [Meta AI](https://ai.meta.com) for LLaMA models
- [Hugging Face](https://huggingface.co) for hosting the model
- [llama.cpp](https://github.com/ggerganov/llama.cpp) for blazing-fast inference
