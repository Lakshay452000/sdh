from pydantic import BaseModel


class RetrievedChunk(BaseModel):
    content: str
    source: str
    node_id: str
    parent_id: str
    level: int
    distance: float
    reranker_score: float | None = None
    bm25_score: float | None = None