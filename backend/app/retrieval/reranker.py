from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(
        self,
        query: str,
        chunks: list,
        top_n: int = 5
    ):

        pairs = [
            (query, chunk.content)
            for chunk in chunks
        ]

        scores = self.model.predict(
            pairs
        )

        scored_chunks = list(
            zip(chunks, scores)
        )

        scored_chunks.sort(
            key=lambda x: x[1],
            reverse=True
        )
        for chunk, score in scored_chunks:
            chunk.reranker_score = float(score)
        return [
            chunk
            for chunk, score
            in scored_chunks[:top_n]
        ]