from app.compression.context_compressor import ContextCompressor
from app.schemas.retrieved_chunk import RetrievedChunk


class KeywordContextCompressor(ContextCompressor):

    def compress(
        self,
        query: str,
        chunks: list[RetrievedChunk]
    ) -> list[RetrievedChunk]:
        return chunks