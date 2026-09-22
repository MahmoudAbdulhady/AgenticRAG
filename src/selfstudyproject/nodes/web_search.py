from selfstudyproject.state import GraphState
from langchain_tavily import TavilySearch
from typing import Dict, Any


def web_search(state: GraphState) -> Dict[str, Any]:
    """Search the web for information"""
    research_query = state["research_query"]
    search = TavilySearch(
        max_results=3,
        search_depth="basic",
    )
    response = search.invoke({"query": research_query})
    results = response.get("results", [])
    web_context = "\n\n".join(
        f"""
Title: {result.get("title", "")}
URL: {result.get("url", "")}
Content: {result.get("content", "")}
""".strip()
        for result in results
    )

    return {"web_context": web_context}
