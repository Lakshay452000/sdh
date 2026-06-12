from fastapi import APIRouter, File, UploadFile

from app.dependencies.architecture import (
    architecture_service
)
from app.architecture.schemas import (
    ArchitectureEvaluationRequest
)
router = APIRouter(
    prefix="/architecture",
    tags=["Architecture"]
)

@router.post("/review")
async def review_diagram(
        file: UploadFile = File(...)
):
    image_bytes = await file.read()

    return await architecture_service.review_diagram(
        image_bytes=image_bytes
    )

@router.post("/evaluate")
async def evaluate_architecture(
        request: ArchitectureEvaluationRequest
):
    return await architecture_service.evaluate(
        architecture_description=request.architecture_description,
        review_findings=request.review_findings
    )