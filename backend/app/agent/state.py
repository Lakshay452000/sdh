from typing import TypedDict


class AgentState(TypedDict):
    user_query: str
    route: str
    tool_result: str
    response: str

    needs_more_info: bool
    iteration_count: int