from app.agent.graph import build_agent_graph


class AgentService:

    def __init__(self):
        self.graph = build_agent_graph()

    def chat(self, query: str):

        result = self.graph.invoke(
            {
                "user_query": query,
                "iteration_count": 0,
                "tool_results": []
            }
        )

        return result["response"]