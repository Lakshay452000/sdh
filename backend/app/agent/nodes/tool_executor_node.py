from app.agent.tools.registry import (
    TOOL_REGISTRY
)


def tool_executor_node(
    state
):
    print("TOOL EXECUTOR")
    route = state["route"]

    tool = (
        TOOL_REGISTRY
        .get(route)
    )

    if tool is None:

        result = (
            f"{route} tool not implemented"
        )

    else:

        result = tool.execute(
            state["user_query"]
        )

    return {
        **state,
        "tool_result": result
    }