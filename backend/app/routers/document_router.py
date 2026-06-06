from pathlib import Path
import tempfile

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)
from app.schemas.document_response import (
    DocumentResponse
)
from app.services.document_service import (
    DocumentService
)
from app.schemas.upload_document_response import (
    UploadDocumentResponse
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

document_service = DocumentService()

@router.post(
    "/upload",
    response_model=UploadDocumentResponse
)
async def upload_document(
    file: UploadFile = File(...)
):

    allowed_extensions = {
        ".pdf",
        ".txt"
    }

    extension = Path(
        file.filename
    ).suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=(
                "Only PDF and TXT files "
                "are supported"
            )
        )

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=extension
    ) as temp_file:

        content = await file.read()

        temp_file.write(content)

        temp_path = Path(
            temp_file.name
        )

    try:

        document_id = (
            document_service.ingest_document(
                temp_path,
                file.filename
            )
        )

        return UploadDocumentResponse(
            document_id=document_id,
            file_name=file.filename,
            message=(
                "Document uploaded "
                "successfully"
            )
        )

    except ValueError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

    finally:

        temp_path.unlink(
            missing_ok=True
        )

@router.get(
    "",
    response_model=list[DocumentResponse]
)
def list_documents():

    return (
        document_service
        .list_documents()
    )

@router.delete(
    "/{document_id}"
)
def delete_document(
    document_id: str
):

    try:

        document_service.delete_document(
            document_id
        )

        return {
            "message":
            "Document deleted successfully"
        }

    except ValueError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )
    
@router.get("/debug/chunks")
def get_chunks():

    return document_service.get_all_chunks()