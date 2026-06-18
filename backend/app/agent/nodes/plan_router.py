from app.agent.state import AgentState


def plan_router(
    state: AgentState
):

    if (
        state["current_step"]
        <
        len(state["plan"])
    ):
        return "tool_executor"

    return "reflection"