from pydantic import BaseModel

from app.schemas.retrieved_chunk import RetrievedChunk


class RagResponse(BaseModel):
    answer: str
    sources: list[str]
    retrieved_chunks: list[RetrievedChunk]