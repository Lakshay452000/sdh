from pydantic import BaseModel


class RetrievedChunk(BaseModel):
    content: str
    source: str
    chunk_number: int
    distance: float
    reranker_score: float | None = None
    bm25_score: float | None = None