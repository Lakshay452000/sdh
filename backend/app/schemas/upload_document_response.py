from pydantic import BaseModel


class UploadDocumentResponse(BaseModel):
    document_id: str
    file_name: str
    message: str