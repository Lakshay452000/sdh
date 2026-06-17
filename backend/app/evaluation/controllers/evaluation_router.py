from fastapi import APIRouter

from app.evaluation.schemas.evaluation_response import (
    EvaluationResponse
)

from app.dependencies.rag_dependencies import (
    ragas_evaluation_service
)

router = APIRouter(
    prefix="/evaluation",
    tags=["Evaluation"]
)


@router.post(
    "/run",
    response_model=EvaluationResponse
)
def run_evaluation():

    result = (
        ragas_evaluation_service
        .run_evaluation()
    )

    return EvaluationResponse(
        faithfulness=result.faithfulness,
        answer_relevancy=result.answer_relevancy,
        context_precision=result.context_precision,
        context_recall=result.context_recall
    )