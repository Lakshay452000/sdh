from app.agent.state import AgentState


def reflection_node(
    state: AgentState
):
    result = state["tool_result"].lower()

    needs_more_info = (
        "could not find" in result
        or
        "no relevant information" in result
    )


    print("REFLECTION")
    print(
        f"needs_more_info={needs_more_info}"
    )
    if state["iteration_count"] >= 2:
        needs_more_info = False

    return {
        **state,
        "needs_more_info": needs_more_info
    }