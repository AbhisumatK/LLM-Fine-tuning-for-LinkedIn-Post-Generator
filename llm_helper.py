# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="meta-llama/llama-4-scout-17b-16e-instruct")

from langchain_groq import ChatGroq
import streamlit as st
import os

api_key = st.secrets["GROQ_API_KEY"]

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)


