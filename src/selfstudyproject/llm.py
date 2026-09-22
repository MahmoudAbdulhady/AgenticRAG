import os 
from langchain_google_genai import ChatGoogleGenerativeAI

def get_generator_llm():
     return ChatGoogleGenerativeAI(
        model=os.getenv("GOOGLE_MODEL"),
        temperature=0.2,
    )


def get_evaluator_llm():
    return ChatGoogleGenerativeAI(
    model=os.getenv("GOOGLE_EVALUATOR_MODEL"),
     temperature=0.2,
    )