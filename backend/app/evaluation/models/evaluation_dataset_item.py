from pydantic import BaseModel


class EvaluationDatasetItem(
    BaseModel
):
    question: str
    ground_truth: str