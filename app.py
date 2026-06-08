import streamlit as st
from reviewer import review_code

st.set_page_config(
    page_title="Code Review Feedback Generator",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Code Review Feedback Generator")

st.write(
    "Paste your code snippet below and get AI-generated review feedback."
)

code = st.text_area(
    "Enter your code:",
    height=300
)

if st.button("Review Code"):

    if not code.strip():
        st.warning("Please enter a code snippet.")
    else:

        with st.spinner("Reviewing code..."):

            result = review_code(code)

        st.subheader("Review Result")

        st.json(result)