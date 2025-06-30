import streamlit as st
from utils import extract_text_from_pdf, ask_ai

# Page settings
# --- Custom CSS Styling ---
def local_css(css):
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

custom_css ="""
body {
    background-color: #f4f6f9;
    font-family: 'Segoe UI',san-serif;
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
    background-color: white;
    box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
    padding: 10px;
}

.css-1d391kg {  /* Main card style */
    border-radius: 12px;
    background-color: white;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    padding: 2rem;
}
"""


local_css(custom_css)

st.set_page_config(page_title="SmartSDLC", layout="centered")
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to:", [
    "🏠 Home",
    "📄 Requirement Classifier",
    "🧠 Code Generator",
    "🐞 Bug Fixer",
    "✅ Test Case Generator",
    "📘 Code Summarizer",
    "💬 Chatbot Assistant"
])
st.title("SmartSDLC – Requirement Classifier")
st.write("Upload a PDF and let AI sort sentences by SDLC phase.")

# Upload button
pdf = st.file_uploader("Upload Requirements PDF", type="pdf")

if pdf:
    # Show a spinner while processing
    with st.spinner("Analyzing PDF..."):
        text = extract_text_from_pdf(pdf)

        prompt = f"""
You are an SDLC assistant.
Classify each sentence in this text into: Requirements, Design, Development, Testing, Deployment.
Group results under headings.

{text}
"""
        ai_output = ask_ai(prompt)

    st.success("Done! Here’s the result:")
    st.text_area("Classified Output", ai_output, height=400)
