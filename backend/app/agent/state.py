from typing import TypedDict


class AgentState(TypedDict):
    user_query: str

    route: str

    plan: list[str]
    current_step: int

    tool_results: list
    response: str

    needs_more_info: bool
    iteration_count: int