from pydantic import BaseModel


class EvaluationResult(
    BaseModel
):
    overall_score: float
    faithfulness: float
    answer_relevancy: float
    context_precision: float
    context_recall: float