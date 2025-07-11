import streamlit as st
from transformers import pipeline

# Load model
chat_pipeline = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Initialize session state
if "memory" not in st.session_state:
    st.session_state.memory = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def chat_with_memory(user_input):
    if "my name is" in user_input.lower():
        name = user_input.split("is")[-1].strip().split()[0]
        st.session_state.memory["name"] = name
        return f"Nice to meet you, {name}! How can I assist you today?"
    if 'name' in st.session_state.memory:
        # personalize
        prompt = f"Hello {st.session_state.memory['name']}, how can I help you?"
        response = chat_pipeline(prompt)
    else:
        response = chat_pipeline(user_input)
    return response[0]['generated_text']

# Title
st.title("💬 Chatbot with Memory")

st.markdown(
    "_Powered by DialoGPT (Microsoft) & HuggingFace 🤗_\n\n"
    "Developed by suryakailash"
)

# Display chat history in nice bubbles
for sender, message in st.session_state.chat_history:
    if sender == "You":
        with st.chat_message("user"):
            st.markdown(message)
    else:
        with st.chat_message("assistant"):
            st.markdown(message)

# User input
if prompt := st.chat_input("Type your message here…"):
    # Append user message
    st.session_state.chat_history.append(("You", prompt))

    # Get bot response
    response = chat_with_memory(prompt)
    st.session_state.chat_history.append(("Bot", response))

    # Show latest exchange
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)

# Optional reset button at the bottom
if st.button("🔄 Reset Chat"):
    st.session_state.chat_history = []
    st.session_state.memory = {}
    st.rerun()
