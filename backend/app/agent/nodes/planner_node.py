from app.agent.state import AgentState


def planner_node(state: AgentState) -> AgentState:
    query = state["user_query"].lower()

    if "review" in query:
        route = "architecture_review"

    elif "evaluate" in query:
        route = "evaluation"

    else:
        route = "rag"

    return {
        **state,
        "route": route
    }