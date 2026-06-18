from app.agent.tools.registry import (
    TOOL_REGISTRY
)


def tool_executor_node(
    state
):
    plan = state["plan"]

    step = plan[
        state["current_step"]
    ]

    tool = TOOL_REGISTRY.get(
        step
    )

    if tool is None:

        result = (
            f"{step} tool not implemented"
        )

    else:

        result = tool.execute(
            state["user_query"]
        )

    tool_results = list(
        state.get(
            "tool_results",
            []
        )
    )

    tool_results.append(
        {
            "step": step,
            "result": result
        }
    )

    return {
        **state,
        "tool_results": tool_results
    }