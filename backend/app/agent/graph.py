from langgraph.graph import StateGraph
from langgraph.graph import END

from app.agent.state import AgentState
from app.agent.nodes.planner_node import planner_node
from app.agent.nodes.responder_node import responder_node


def build_agent_graph():

    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("responder", responder_node)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "responder")
    graph.add_edge("responder", END)

    return graph.compile()