from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

import os

from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """You are helpful assisatnt, please response to the queries asked by the user and respond it
                   quickly. If you don't know the answer then say Sorry i did't give you appropriate answer about it.
                   "And if you know the answer give the answer and in last say Thank you for asking!!!"""),
        ("user", "Question:{question}")
    ]
)

# Streamlit 

st.title("Hey There i'm the Assistant to Help you!")
input_text = st.text_input("Seach here")

# Model
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
