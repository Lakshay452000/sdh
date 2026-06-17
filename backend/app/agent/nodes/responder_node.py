from app.agent.state import AgentState


def responder_node(state: AgentState) -> AgentState:

    route = state["route"]

    if route == "architecture_review":
        response = "Architecture review selected"

    elif route == "evaluation":
        response = "Evaluation selected"

    else:
        response = "RAG selected"

    return {
        **state,
        "response": response
    }