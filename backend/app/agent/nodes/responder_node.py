from app.agent.state import AgentState


def responder_node(
    state: AgentState
) -> AgentState:

    results = (
        state.get(
            "tool_results",
            []
        )
    )

    response = "\n\n".join(
        [
            f"{item['step']}:\n{item['result']}"
            for item in results
        ]
    )

    return {
        **state,
        "response": response
    }