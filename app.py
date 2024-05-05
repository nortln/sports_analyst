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
You are to analyze the two basketball games i will be giving you today thoroughly and give the predictions in the following format.
you will analyze the game based on their past 5 games and get the safest prediction.
team to win :
points in 1st half :
points in full game : 
"""


if submit:
    response = get_gemini_response(input_prompt, input)
    st.subheader("The Prediction is")
    st.write(response)