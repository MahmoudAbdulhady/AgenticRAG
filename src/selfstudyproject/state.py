from typing import TypedDict
from langchain_core.documents import Document


class GraphState(TypedDict , total=False):
    """Graph State 
    
    Attributes:
        question: str
    documents: list[Document]
    answer: str
    evaluation_reason: str
    needs_research: bool
    research_query: str
    web_context: str


    Answer should be in the following format:
    {
        "answer": "The answer to the question",
        "evaluation_reason": "The reason for the answer",
        "needs_research": "True or False",
        "research_query": "The query to research",
        "web_context": "The web context"
    }
    """

    question: str
    documents: list[Document]
    answer: str
    evaluation_reason: str
    needs_research: bool
    research_query: str
    web_context: str

