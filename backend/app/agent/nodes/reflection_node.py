from app.agent.state import AgentState


def reflection_node(
    state: AgentState
):

    latest_result = (
        state["tool_results"][-1]["result"]
    )

    result = (
        latest_result.lower()
    )

    needs_more_info = (
        "could not find" in result
        or
        "no relevant information" in result
    )

    if state["iteration_count"] >= 2:
        needs_more_info = False

    return {
        **state,
        "needs_more_info": needs_more_info
    }