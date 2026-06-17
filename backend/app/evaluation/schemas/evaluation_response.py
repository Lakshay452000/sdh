from pydantic import BaseModel


class EvaluationResponse(
    BaseModel
):
    faithfulness: float
    answer_relevancy: float
    context_precision: float
    context_recall: float