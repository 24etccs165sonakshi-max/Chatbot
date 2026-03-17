import google.generativeai as genai
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
# Configure API key from Streamlit Secrets
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Make sure this model supports generate_content
model = genai.GenerativeModel("gemini-2.5-flash")


def my_output(query: str) -> str:
    if not query.strip():
        return "Please enter a query."
    response = model.generate_content(query)
    return response.text

# UI Development using streamlit

# Streamlit UI
st.set_page_config(page_title="QUERY_BOT")
st.header("QUERY_BOT")

input_text = st.text_input("Enter your query:", key="input")
submit = st.button("Ask your query")

if submit:
    result = my_output(input_text)
    st.subheader("Response:")
    st.write(result)