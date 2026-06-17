from pydantic import BaseModel


class EvaluationSample(
    BaseModel
):
    question: str
    ground_truth: str
    answer: str
    contexts: list[str]