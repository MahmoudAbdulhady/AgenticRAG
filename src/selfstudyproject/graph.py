from dotenv import load_dotenv
load_dotenv()
from langgraph.graph import StateGraph, START, END
from selfstudyproject.nodes.evaluate_answer import evaluate_answer
from selfstudyproject.nodes.generate_answer import generate_answer
from selfstudyproject.nodes.web_search import web_search
from selfstudyproject.nodes.retrieve import retrieve_documents
from selfstudyproject.nodes.regenerate_answer import regenerate_answer
from selfstudyproject.routing import route_after_evaluation
from selfstudyproject.state import GraphState

def create_graph():
    builder = StateGraph(GraphState)
    # Nodes
    builder.add_node("retrieve" , retrieve_documents)
    builder.add_node("generate_answer", generate_answer)
    builder.add_node("evaluate_answer", evaluate_answer)
    builder.add_node("web_search", web_search)
    builder.add_node("regenerate_answer", regenerate_answer)

    # Edges
    builder.add_edge(START,"retrieve")
    builder.add_edge("retrieve" , "generate_answer")
    builder.add_edge("generate_answer" , "evaluate_answer")

    # Conditional Edges
    builder.add_conditional_edges("evaluate_answer", route_after_evaluation, {
        "accept": END,
        "needs_research": "web_search",
    })

    # Edges from Conditional Edges
    builder.add_edge("web_search" , "regenerate_answer")
    builder.add_edge("regenerate_answer" , END)

    return builder.compile()

