from typing import Dict, Any
from selfstudyproject.llm import get_generator_llm
from selfstudyproject.state import GraphState
from langchain_core.prompts import ChatPromptTemplate



def regenerate_answer(state: GraphState) -> Dict[str, Any]:
    """Regenerate the answer"""
    question = state["question"]
    documents = state["documents"]
    web_context = state["web_context"]
    retrieved_context = "\n\n".join(
        document.page_content
        for document in documents
    )
    llm = get_generator_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are a research assistant.

A previous answer was determined to need additional research.

Generate a new final answer using all available evidence:
- The originally retrieved context
- The additional web research

Use the web research to fill gaps, clarify missing information,
or provide more current information when necessary.

Do not invent facts.
If the available evidence is still insufficient, clearly state that.
"""
            ),
            (
                "human",
                """
Question:
{question}

Retrieved Context:
{retrieved_context}

Web Research:
{web_context}
"""
            ),
        ]
    )
    chain = prompt | llm
    response = chain.invoke({
        "question": question,
        "retrieved_context": retrieved_context,
        "web_context": web_context,
    })

    return {"answer": response.content}
