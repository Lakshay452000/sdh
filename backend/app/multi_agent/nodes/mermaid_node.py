from app.multi_agent.state import (
    ArchitectureWorkflowState
)

from app.multi_agent.agent_registry import (
    mermaid_agent
)


async def mermaid_node(
    state: ArchitectureWorkflowState
):

    diagram = await (
        mermaid_agent.execute(
            state["correction"]
            .corrected_architecture
        )
    )

    return {
        **state,
        "mermaid_diagram":
            diagram.mermaid_diagram
    }