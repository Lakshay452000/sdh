from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):
        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def score(
        self,
        query: str,
        texts: list[str]
    ) -> list[float]:

        if not texts:
            return []

        pairs = [
            (query, text)
            for text in texts
        ]

        return list(
            self.model.predict(pairs)
        )

    def rerank(
        self,
        query: str,
        chunks: list,
        top_n: int = 5
    ):

        if not chunks:
            return []

        scores = self.score(
            query=query,
            texts=[
                chunk.content
                for chunk in chunks
            ]
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
            for chunk, _
            in scored_chunks[:top_n]
        ]