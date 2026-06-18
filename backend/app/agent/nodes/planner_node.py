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
    
    if (
        state.get("plan")
        and
        state["iteration_count"] > 0
    ):
        return {
            **state,
            "iteration_count":
                state["iteration_count"] + 1
        }
    
    query = (
        state["user_query"]
        .lower()
    )

    if "review" in query:

        plan = [
            "architecture_review",
            "evaluation"
        ]

    elif "evaluate" in query:

        plan = [
            "evaluation"
        ]

    elif any(
        keyword in query
        for keyword in MEMORY_KEYWORDS
    ):

        plan = [
            "memory"
        ]

    else:

        plan = [
            "rag"
        ]

    return {
        **state,
        "plan": plan,
        "current_step": 0,
        "iteration_count":
            state.get(
                "iteration_count",
                0
            ) + 1
    }