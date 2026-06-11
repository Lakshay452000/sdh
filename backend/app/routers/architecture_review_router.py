from fastapi import APIRouter, File, UploadFile

from app.dependencies.architecture_review import (
    architecture_review_service
)

router = APIRouter(
    prefix="/architecture-review",
    tags=["Architecture Review"]
)

@router.post("/review")
async def review_diagram(
        file: UploadFile = File(...)
):
    image_bytes = await file.read()

    return await architecture_review_service.review_diagram(
        image_bytes=image_bytes
    )