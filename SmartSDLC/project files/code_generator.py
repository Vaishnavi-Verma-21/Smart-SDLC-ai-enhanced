import streamlit as st
from utils import generate_code

# UI settings
st.set_page_config(page_title="AI Code Generator", layout="centered")
st.title("🤖 SmartSDLC – AI Code Generator")

# Prompt input
user_prompt = st.text_area("Describe what code you need:", height=150)

if st.button("Generate Code"):
    if user_prompt.strip():
        with st.spinner("Generating code..."):
            result = generate_code(user_prompt)
        st.success("Done! Here's the generated code:")
        st.code(result, language="python")
    else:
        st.warning("Please enter a prompt to generate code.")
