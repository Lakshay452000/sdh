from app.multi_agent.agent_registry import (
    review_agent
)

from app.multi_agent.state import (
    ArchitectureWorkflowState
)


async def review_node(
    state: ArchitectureWorkflowState
):

    review = await (
        review_agent.execute(
            state["image_bytes"]
        )
    )

    return {
        **state,
        "review": review
    }