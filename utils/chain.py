import streamlit as st
from langchain_cohere import ChatCohere
import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils.prompt import TRAVEL_PROMPT

load_dotenv()

def get_api_key():
    try:
        return st.secrets["COHERE_API_KEY"]
    except Exception:
        return os.getenv("COHERE_API_KEY")

cohere_api_key = get_api_key()

# 1. LLM
llm = ChatCohere(
    cohere_api_key= cohere_api_key,
    model="command-a-03-2025"
)

# 2. Prompt
prompt = PromptTemplate(
    input_variables=["destination", "budget", "days", "travel_type"],
    template=TRAVEL_PROMPT
)

# 3. Output parser (important in LCEL)
parser = StrOutputParser()

# 4. LCEL Chain (this is the new way)
chain = prompt | llm | parser


# 5. Function wrapper
def generate_plan(destination, budget, days, travel_type):
    return chain.invoke({
        "destination": destination,
        "budget": budget,
        "days": days,
        "travel_type": travel_type
    })