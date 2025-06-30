import streamlit as st
from utils import ai_chatbot

st.set_page_config(page_title="SmartSDLC Chatbot Assistant", layout="centered")
st.title("💬 SmartSDLC – Floating Chatbot Assistant")

# Chat history stored in Streamlit session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask me anything about SDLC 👇")

if user_input:
    with st.spinner("Thinking..."):
        answer = ai_chatbot(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("AI", answer))

# Show chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 AI:** {message}")
