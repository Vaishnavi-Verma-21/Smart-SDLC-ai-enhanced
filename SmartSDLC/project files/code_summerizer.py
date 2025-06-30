#import streamlit as st
#from utils import summarize_code

#st.set_page_config(page_title="Code Summarizer", layout="centered")

#st.title("🔎 Code Summarizer")
#st.markdown("Paste Python code below to generate a beginner-friendly summary.")

# Text input for code
#user_code = st.text_area("✍️ Enter your Python code here", height=250)

# On button click, summarize the code
##   if user_code.strip():
  #      with st.spinner("Summarizing..."):
           
        #  summary = summarize_code(user_code)
    #st.subheader("📝 Summary:")
          #  st.success(summary)
    #else:
       # st.warning("Please enter some Python code to summarize.")

import streamlit as st
import requests

st.set_page_config(page_title="Code Summarizer", layout="centered")

st.title("🔵 Code Summarizer")
st.markdown("Paste Python code below to generate a beginner-friendly summary.")

code_input = st.text_area("Paste your code here:")

if st.button("Summarize Code"):
    if code_input.strip():
        with st.spinner("Summarizing..."):
            response = requests.post(
                "http://127.0.0.1:8000/ai/summarize",
                data={"code": code_input}
            )
            if response.ok:
                summary = response.json().get("summary", "No summary generated.")
                st.success("Summary:")
                st.write(summary)
            else:
                st.error("Failed to summarize code.")
    else:
        st.warning("Please enter some code.")


