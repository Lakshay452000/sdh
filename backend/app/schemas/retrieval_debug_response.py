from pydantic import BaseModel

from app.schemas.retrieved_chunk import (
    RetrievedChunk
)


class RetrievalDebugResponse(BaseModel):
    question: str
    retrieved_chunks: list[RetrievedChunk]