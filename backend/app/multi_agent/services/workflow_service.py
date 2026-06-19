from app.multi_agent.graph import (
    build_workflow
)


class WorkflowService:

    def __init__(self):

        self._graph = (
            build_workflow()
        )

    async def execute(
        self,
        architecture_description: str,
        image_bytes: bytes
    ):

        result = await (
            self._graph.ainvoke(
                {
                    "architecture_description":
                        architecture_description,

                    "image_bytes":
                        image_bytes
                }
            )
        )

        return result