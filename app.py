import os
import streamlit as st
from llama_cpp import Llama
from huggingface_hub import hf_hub_download

# Set model info
REPO_ID = "MLP-KTLim/llama-3-Korean-Bllossom-8B-gguf-Q4_K_M"
MODEL_FILE = "llama-3-Korean-Bllossom-8B-Q4_K_M.gguf"

# Download model from HuggingFace if not already downloaded
local_model_path = os.path.join("models", MODEL_FILE)
if not os.path.exists(local_model_path):
    st.warning("Downloading model... please wait (5GB+)...")
    local_model_path = hf_hub_download(
        repo_id=REPO_ID,
        filename=MODEL_FILE,
        local_dir="models",
        local_dir_use_symlinks=False
    )


llm = Llama(
    model_path=local_model_path,
    n_ctx=4096,
    verbose=True
)

# Streamlit UI
st.title(" NCERT-GPT")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", "")

if st.button("Send") and user_input.strip():
    # Generate response from the model
    with st.spinner("Thinking..."):
        response = llm(
            prompt=f"User: {user_input}\nAssistant:",
            max_tokens=512,
            stop=["User:", "Assistant:"]
        )
        answer = response["choices"][0]["text"].strip()
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", answer))

# Display chat history
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {msg}")
