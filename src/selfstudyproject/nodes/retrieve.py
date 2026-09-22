from selfstudyproject.state import GraphState
from typing import Dict , Any
from selfstudyproject.chroma_store import get_vector_store


def retrieve_documents(state: GraphState) -> Dict[str, Any]:
    """Retrieve documents from the vector store"""
    question = state["question"]
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    documents = retriever.invoke(question)
    return {**state,"documents": documents}


