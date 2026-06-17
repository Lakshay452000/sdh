from typing import TypedDict


class AgentState(TypedDict):
    user_query: str
    route: str
    response: str