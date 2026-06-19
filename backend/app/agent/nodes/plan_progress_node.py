from app.agent.state import AgentState


def plan_progress_node(
    state: AgentState
):
    return {
        **state,
        "current_step":
            state["current_step"] + 1
    }