from app.compression.context_compressor import ContextCompressor
from app.schemas.retrieved_chunk import RetrievedChunk


class ContextCompressionService:

    def __init__(
        self,
        compressor: ContextCompressor
    ):
        self._compressor = compressor

    def compress(
        self,
        query: str,
        chunks: list[RetrievedChunk]
    ) -> list[RetrievedChunk]:
        return self._compressor.compress(
            query=query,
            chunks=chunks
        )