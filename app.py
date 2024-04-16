from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def get_gemini_response(input, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([input, prompt])
    return response.text



st.set_page_config("Basketball Analyst")

st.header("Basketball Analyst")
input = st.text_input("Input Prompt: ", key="input")

submit = st.button("Generate")

input_prompt = """
You are a very powerful Basketball Sports analyst. Your work is to
tell who is more likely to win between two teams and their percentage chances of winnning
based on their history, and what other people think.
You will tell what each team will score in the
First half: Over and Under for each team
Second Half: Over and Under for each team
"""

if submit:
    response = get_gemini_response(input_prompt, input)
    st.subheader("The Prediction is")
    st.write(response)