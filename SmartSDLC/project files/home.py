import streamlit as st
from api_client import send_chat_message
from streamlit_lottie import st_lottie
import json
import os
from utils import (
    summarize_code,
    ask_ai,
    generate_code,
    fix_buggy_code,
    generate_test_cases,
    ai_chatbot
)

# --- Page Configuration ---
st.set_page_config(page_title="SmartSDLC", layout="wide")

# --- Helper: Load Lottie Animation ---
def load_lottie_animation(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

# --- Apply Custom CSS Styling ---
def local_css(css):
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

custom_css = """
body {
    background-color: #f4f6f9;
    font-family: 'Segoe UI', sans-serif;
}

h1, h2, h3 {
    color: #003366;
}

.stButton>button {
    background-color: #004080;
    color: white;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
}

.stTextArea, .stTextInput {
    border-radius: 10px;
    background-color: black;
    box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
    padding: 10px;
}

section.main > div {
    padding: 2rem;
    background-color: white;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
"""

local_css(custom_css)

# --- Sidebar Navigation ---
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to:", [
    "🏠 Home",
    "📄 Requirement Classifier",
    "🧠 AI Code Generator",
    "🐞 Bug Fixer",
    "✅ Test Case Generator",
    "📘 Code Summarizer",
    "💬 Chatbot Assistant"
])

# --- 🏠 Home Page ---
if page == "🏠 Home":
    with st.container():
        col1, col2 = st.columns([1, 2])

        with col1:
            lottie = load_lottie_animation("asset/animation.json")
            if lottie:
                st_lottie(lottie, speed=1, loop=True, quality="high", height=300)
            else:
                st.warning("Lottie animation not found. Please check 'asset/animation.json'.")

        with col2:
            st.title("SmartSDLC - AI-Enhanced Software Development Lifecycle")
            st.markdown("""
                Welcome to **SmartSDLC**, your intelligent assistant for every stage of the software development lifecycle.

                Use the left sidebar to explore features like:

                - 📄 Requirement Classifier  
                - 🧠 AI Code Generator  
                - 🐞 Bug Fixer  
                - ✅ Test Case Generator  
                - 📘 Code Summarizer  
                - 💬 Floating Chatbot Assistant  
            """)

# --- 📄 Requirement Classifier ---
elif page == "📄 Requirement Classifier":
    with st.container():
        st.title("📄 Requirement Classifier")
        st.markdown("### Upload Requirement Text or Paste Below")
        text_input = st.text_area("Enter your software requirements here:")
        if st.button("Classify Requirements"):
            if text_input.strip():
                with st.spinner("Classifying..."):
                    result = ask_ai(text_input)
                    st.success("✅ Classified Requirements:")
                    st.write(result)
            else:
                st.warning("Please provide some input.")

# --- 🧠 AI Code Generator ---
elif page == "🧠 AI Code Generator":
    with st.container():
        st.title("🧠 AI Code Generator")
        st.markdown("### Describe What You Want to Build")
        prompt = st.text_area("E.g., 'Build a Python function that adds two numbers'")

        if st.button("Generate Code"):
            if prompt.strip():
                with st.spinner("Generating code..."):
                    code = generate_code(prompt)
                    st.success("✅ Generated Code:")
                    st.code(code, language="python")
            else:
                st.warning("Please enter a description.")

# --- 🐞 Bug Fixer ---
elif page == "🐞 Bug Fixer":
    with st.container():
        st.title("🐞 Bug Fixer")
        st.markdown("### Paste Buggy Code Below")
        buggy_code = st.text_area("Buggy Python code:", height=200)
        if st.button("Fix Bugs"):
            if buggy_code.strip():
                with st.spinner("Fixing bugs..."):
                    fixed = fix_buggy_code(buggy_code)
                    st.success("✅ Fixed Code:")
                    st.code(fixed, language="python")
            else:
                st.warning("Please enter some code.")

# --- ✅ Test Case Generator ---
elif page == "✅ Test Case Generator":
    with st.container():
        st.title("✅ Test Case Generator")
        st.markdown("### Paste Your Function/Code Below")
        code_for_tests = st.text_area("Python code for which you want test cases", height=200)
        if st.button("Generate Test Cases"):
            if code_for_tests.strip():
                with st.spinner("Generating test cases..."):
                    tests = generate_test_cases(code_for_tests)
                    st.success("✅ Test Cases:")
                    st.code(tests, language="python")
            else:
                st.warning("Please enter some code.")

# --- 📘 Code Summarizer ---
elif page == "📘 Code Summarizer":
    with st.container():
        st.title("📘 Code Summarizer")
        code = st.text_area("Paste your Python code:", height=200)
        if st.button("Summarize"):
            if code.strip():
                with st.spinner("Summarizing..."):
                    summary = summarize_code(code)
                    st.success("✅ Summary:")
                    st.write(summary)
            else:
                st.warning("Please enter some code.")

# --- 💬 Chatbot Assistant ---
elif page == "💬 Chatbot Assistant":
    with st.container():
        st.title("💬 Floating Chatbot Assistant")
        st.markdown("### Ask Something About Software Development")
        query = st.text_input("Ask your question:")
        if st.button("Ask"):
            if query.strip():
                with st.spinner("Asking AI..."):
                    reply = ai_chatbot(query)
                    st.success("💬 AI Response:")
                    st.write(reply)
            else:
                st.warning("Please enter a question.")

# --- 💬 Floating Smart Chatbot in Sidebar ---
with st.sidebar:
    st.markdown("---")
    st.header("💬 Smart Chatbot")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    with st.form("chat_form", clear_on_submit=True):
        user_message = st.text_input("You 👤", placeholder="Ask something...")
        submitted = st.form_submit_button("Send")

        if submitted and user_message:
            st.session_state.chat_history.append(("user", user_message))

            with st.spinner("🤖 AI is typing..."):
                response = send_chat_message(user_message)
                bot_reply = response.get("reply", "Sorry, I couldn't understand that.")
                st.session_state.chat_history.append(("ai", bot_reply))

    # Show last 10 messages
    st.session_state.chat_history = st.session_state.chat_history[-10:]

    for role, message in reversed(st.session_state.chat_history):
        if role == "user":
            st.markdown(f"👤 **You**: {message}")
        else:
            st.markdown(f"🤖 **AI**: {message}")
