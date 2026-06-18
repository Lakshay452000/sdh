from app.agent.state import AgentState


def responder_node(
    state: AgentState
) -> AgentState:
    print("RESPONDER")
    return {
        **state,
        "response": state["tool_result"]
    }