from pydantic import BaseModel

from app.schemas.retrieved_chunk import (
    RetrievedChunk
)


class AskResponse(BaseModel):
    question: str
    answer: str
    sources: list[str]
    retrieved_chunks: list[RetrievedChunk]