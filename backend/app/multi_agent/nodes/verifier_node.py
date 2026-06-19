from app.multi_agent.state import (
    ArchitectureWorkflowState
)
from app.multi_agent.agent_registry import (
    verifier_agent
)

async def verifier_node(
    state: ArchitectureWorkflowState
):

    verification = await (
        verifier_agent.execute(
            review=state["review"],
            correction=state["correction"]
        )
    )

    return {
        **state,
        "verification": verification
    }