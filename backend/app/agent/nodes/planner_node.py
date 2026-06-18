from app.agent.state import AgentState


MEMORY_KEYWORDS = [
    "remember",
    "memory",
    "earlier",
    "previous",
    "history",
    "what did we discuss"
]


def planner_node(
    state: AgentState
) -> AgentState:
    print("PLANNER")
    query = (
        state["user_query"]
        .lower()
    )

    if "review" in query:

        route = (
            "architecture_review"
        )

    elif "evaluate" in query:

        route = "evaluation"

    elif any(
        keyword in query
        for keyword in MEMORY_KEYWORDS
    ):

        route = "memory"

    else:

        route = "rag"

    return {
        **state,
        "route": route,
        "iteration_count":
            state.get(
                "iteration_count",
                0
            ) + 1
    }