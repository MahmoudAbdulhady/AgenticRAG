from multiprocessing import context
from typing import Dict, Any

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from selfstudyproject.llm import get_evaluator_llm
from selfstudyproject.state import GraphState




class EvaluationResult(BaseModel):
    evaluation_reason: str = Field(
        description="Explain why the answer is sufficient or insufficient."
    )

    needs_research: bool = Field(
        description="True if additional web research is needed, otherwise False."
    )

    research_query: str = Field(
        description="A focused web search query if research is needed. Otherwise return an empty string."
    )



def evaluate_answer(state: GraphState) -> Dict[str, Any]:
    """Evaluate the answer to the question"""
    llm = get_evaluator_llm()
    question = state["question"]
    answer = state["answer"]
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
You are an evaluator for a retrieval-augmented generation system.

Your job is to determine whether the generated answer sufficiently
answers the user's question based on the retrieved context.

Mark needs_research as False when:
- The answer addresses the user's question.
- The answer is supported by the retrieved context.
- The retrieved context contains enough information.

Mark needs_research as True when:
- The retrieved context is insufficient.
- Important information is missing.
- The answer is unsupported by the retrieved context.
- Additional or current information is required.

If additional research is required, create a focused search query.
Otherwise, return an empty research_query.
"""
            ),
            (
                "human",
                """
Question:
{question}

Retrieved Context:
{context}

Generated Answer:
{answer}
"""
            )
        ]
    )
    structured_llm = llm.with_structured_output(EvaluationResult)
    chain = prompt | structured_llm
    response = chain.invoke(
        {
            "question": question,
            "context": context,
            "answer": answer
        }
    )
    result = {
        "evaluation_reason": response.evaluation_reason,
        "needs_research": response.needs_research,
        "research_query": response.research_query
    }
    return result

