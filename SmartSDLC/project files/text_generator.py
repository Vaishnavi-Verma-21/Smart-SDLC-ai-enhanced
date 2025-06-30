import streamlit as st
from utils import generate_test_cases

st.set_page_config(page_title="Test Case Generator", layout="centered")
st.title("🧪 SmartSDLC – Test Case Generator")

user_code = st.text_area("Paste your functional Python code:", height=250)

if st.button("Generate Test Cases"):
    if user_code.strip():
        with st.spinner("Generating test cases..."):
            test_cases = generate_test_cases(user_code)
        st.success("Here are your AI-generated test cases:")
        st.code(test_cases, language="python")
    else:
        st.warning("Please enter some functional code.")
