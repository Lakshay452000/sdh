from abc import ABC, abstractmethod

from app.schemas.retrieved_chunk import RetrievedChunk


class ContextCompressor(ABC):

    @abstractmethod
    def compress(
        self,
        query: str,
        chunks: list[RetrievedChunk]
    ) -> list[RetrievedChunk]:
        raise NotImplementedError