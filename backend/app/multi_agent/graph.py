from langgraph.graph import (
    StateGraph,
    END
)

from app.multi_agent.state import (
    ArchitectureWorkflowState
)

from app.multi_agent.nodes.review_node import (
    review_node
)

from app.multi_agent.nodes.evaluation_node import (
    evaluation_node
)

from app.multi_agent.nodes.correction_node import (
    correction_node
)

from app.multi_agent.nodes.verifier_node import (
    verifier_node
)
from app.multi_agent.nodes.mermaid_node import (
    mermaid_node
)


def build_workflow():

    graph = StateGraph(
        ArchitectureWorkflowState
    )

    graph.add_node(
        "review",
        review_node
    )

    graph.add_node(
        "evaluation",
        evaluation_node
    )

    graph.add_node(
        "correction",
        correction_node
    )

    graph.add_node(
        "verification",
        verifier_node
    )
    graph.add_node(
        "mermaid",
        mermaid_node
    )

    graph.set_entry_point(
        "review"
    )

    graph.add_edge(
        "review",
        "evaluation"
    )

    graph.add_edge(
        "evaluation",
        "correction"
    )

    graph.add_edge(
        "correction",
        "verification"
    )

    graph.add_edge(
        "verification",
        "mermaid"
    )

    graph.add_edge(
        "mermaid",
        END
    )

    return graph.compile()