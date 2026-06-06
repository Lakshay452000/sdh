from pydantic import BaseModel


class FilterDebugRequest(BaseModel):
    question: str
    document_id: str