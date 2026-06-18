from langgraph.graph import StateGraph
from langgraph.graph import END

from app.agent.state import AgentState

from app.agent.nodes.planner_node import (
    planner_node
)

from app.agent.nodes.tool_executor_node import (
    tool_executor_node
)

from app.agent.nodes.reflection_node import (
    reflection_node
)

from app.agent.nodes.reflection_router import (
    reflection_router
)

from app.agent.nodes.responder_node import (
    responder_node
)
from app.agent.nodes.plan_progress_node import (
    plan_progress_node
)

from app.agent.nodes.plan_router import (
    plan_router
)

def build_agent_graph():

    graph = StateGraph(AgentState)

    graph.add_node(
        "planner",
        planner_node
    )

    graph.add_node(
        "tool_executor",
        tool_executor_node
    )

    graph.add_node(
        "reflection",
        reflection_node
    )

    graph.add_node(
        "responder",
        responder_node
    )
    graph.add_node(
        "plan_progress",
        plan_progress_node
    )
    graph.set_entry_point(
        "planner"
    )
    graph.add_edge(
        "planner",
        "tool_executor"
    )
    graph.add_edge(
        "tool_executor",
        "plan_progress"
    )

    graph.add_conditional_edges(
        "reflection",
        reflection_router,
        {
            "planner": "planner",
            "responder": "responder"
        }
    )
    graph.add_conditional_edges(
        "plan_progress",
        plan_router,
        {
            "tool_executor":
                "tool_executor",

            "reflection":
                "reflection"
        }
    )

    graph.add_edge(
        "responder",
        END
    )

    return graph.compile()