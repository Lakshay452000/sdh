from pydantic import BaseModel


class WorkflowResponse(
    BaseModel
):
    review: dict
    evaluation: dict
    correction: dict
    verification: str