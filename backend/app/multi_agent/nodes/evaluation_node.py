from app.multi_agent.state import (
    ArchitectureWorkflowState
)
from app.multi_agent.agent_registry import (
    evaluation_agent
)

async def evaluation_node(
    state: ArchitectureWorkflowState
):

    evaluation = await (
        evaluation_agent.execute(
            architecture_description=
                state[
                    "architecture_description"
                ],
            review_findings=
                state["review"]
                    .model_dump_json()
        )
    )

    return {
        **state,
        "evaluation": evaluation
    }