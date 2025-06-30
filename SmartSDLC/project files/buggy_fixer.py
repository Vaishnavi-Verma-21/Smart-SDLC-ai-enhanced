import streamlit as st
from utils import fix_buggy_code

st.set_page_config(page_title="Bug Fixer", layout="centered")
st.title("🛠️ SmartSDLC – Bug Fixer")

buggy_code = st.text_area("Paste your buggy Python/JS code here:", height=250)

if st.button("Fix My Code"):
    if buggy_code.strip():
        with st.spinner("Analyzing and fixing..."):
            fixed_code = fix_buggy_code(buggy_code)
        st.success("Here’s the fixed code:")
        st.code(fixed_code, language="python")
    else:
        st.warning("Please paste some buggy code.")
