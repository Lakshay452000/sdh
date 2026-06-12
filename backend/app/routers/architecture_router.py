from fastapi import APIRouter, File, UploadFile

from app.dependencies.architecture import (
    architecture_service
)
from app.architecture.schemas import (
    ArchitectureEvaluationRequest,
    MermaidDiagramRequest,
    ArchitectureDiagram,
)

from app.architecture.schemas import (
    ArchitectureCorrection,
    ArchitectureCorrectionRequest
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

@router.post(
    "/correct",
    response_model=ArchitectureCorrection
)
async def correct_architecture(
    request: ArchitectureCorrectionRequest
):
    return await architecture_service.generate_corrections(
        architecture_description=request.architecture_description,
        review=request.review,
        evaluation=request.evaluation
    )

@router.post(
    "/correct",
    response_model=ArchitectureCorrection
)
async def correct_architecture(
    request: ArchitectureCorrectionRequest
):
    return await architecture_service.generate_corrections(
        architecture_description=request.architecture_description,
        review=request.review,
        evaluation=request.evaluation
    )

@router.post(
    "/mermaid",
    response_model=ArchitectureDiagram
)
async def generate_mermaid(
    request: MermaidDiagramRequest
):
    return await architecture_service.generate_mermaid_diagram(
        architecture_description=request.architecture_description
    )