from selfstudyproject.state import GraphState
from typing import Literal


def route_after_evaluation(state: GraphState) -> Literal["accept" , "needs_research"]:
    if state["needs_research"]:
        return "needs_research"
    else:
        return "accept"
