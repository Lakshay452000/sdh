import re
import math

from app.compression.context_compressor import ContextCompressor
from app.schemas.retrieved_chunk import RetrievedChunk


from app.retrieval.reranker import Reranker


class SentenceRerankerCompressor(ContextCompressor):

    def __init__(
        self,
        reranker: Reranker,
        keep_ratio: float
    ):
        self._reranker = reranker
        self._keep_ratio = keep_ratio

    def compress(
        self,
        query: str,
        chunks: list[RetrievedChunk]
    ) -> list[RetrievedChunk]:

        compressed_chunks: list[RetrievedChunk] = []

        for chunk in chunks:

            compressed_content = self._compress_chunk(
                query=query,
                content=chunk.content
            )

            compressed_chunks.append(
                chunk.model_copy(
                    update={
                        "content": compressed_content
                    }
                )
            )

        return compressed_chunks

    def _compress_chunk(
        self,
        query: str,
        content: str
    ) -> str:
        
        sentences = self._split_sentences(
            content
        )
        
        if len(sentences) <= 3:
            return content

        scores = self._reranker.score(
            query=query,
            texts=sentences
        )

        scored_sentences = list(
            enumerate(
                zip(sentences, scores)
            )
        )

        scored_sentences.sort(
            key=lambda item: item[1][1],
            reverse=True
        )

        sentences_to_keep = max(
            1,
            math.ceil(
                len(sentences)
                * self._keep_ratio
            )
        )

        selected_indexes = sorted([
            index
            for index, _
            in scored_sentences[
                :sentences_to_keep
            ]
        ])

        compressed_sentences = [
            sentences[index]
            for index in selected_indexes
        ]

        return " ".join(
            compressed_sentences
        )

    @staticmethod
    def _split_sentences(
        text: str
    ) -> list[str]:
        return [
            sentence.strip()
            for sentence in re.split(
                r'(?<=[.!?])\s+',
                text
            )
            if sentence.strip()
        ]