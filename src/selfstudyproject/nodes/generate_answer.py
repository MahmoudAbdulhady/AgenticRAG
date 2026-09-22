from selfstudyproject.state import GraphState
from typing import Dict, Any
from langchain_core.prompts import ChatPromptTemplate
from selfstudyproject.llm import get_generator_llm


def generate_answer(state: GraphState) -> Dict[str, Any]:
    """Generate an answer to the question"""
    llm = get_generator_llm()
    question = state["question"]
    documents = state["documents"]
    context = "\n\n".join(
        document.page_content
        for document in documents
    )
    
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are a helpful research assistant.

Answer the user's question using only the provided context.

If the context is insufficient to answer the question,
say that the available context is insufficient.

Do not invent information.
"""
            ),
            (
                "human",
                """
Question:
{question}

Context:
{context}
"""
            )
        ]
    )
    chain = prompt | llm
    response = chain.invoke({"question": question, "context": context})
    return {**state, "answer": response.content}