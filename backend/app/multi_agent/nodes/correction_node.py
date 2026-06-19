from app.multi_agent.state import (
    ArchitectureWorkflowState
)
from app.multi_agent.agent_registry import (
    correction_agent
)

async def correction_node(
    state: ArchitectureWorkflowState
):

    correction = await (
        correction_agent.execute(
            architecture_description=
                state[
                    "architecture_description"
                ],
            review=
                state["review"],
            evaluation=
                state["evaluation"]
        )
    )

    return {
        **state,
        "correction": correction
    }