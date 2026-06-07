from app.schemas.retrieved_chunk import (
    RetrievedChunk
)


def reciprocal_rank_fusion(
    vector_chunks: list[RetrievedChunk],
    bm25_chunks: list[RetrievedChunk],
    k: int = 60
) -> list[RetrievedChunk]:

    scores = {}

    chunk_map = {}

    for rank, chunk in enumerate(
        vector_chunks,
        start=1
    ):

        score = (
            1 /
            (k + rank)
        )

        scores[
            chunk.node_id
        ] = score

        chunk_map[
            chunk.node_id
        ] = chunk

    for rank, chunk in enumerate(
        bm25_chunks,
        start=1
    ):

        score = (
            1 /
            (k + rank)
        )

        scores[chunk.node_id] = (
            scores.get(chunk.node_id, 0) + score
        )

        if (
            chunk.node_id
            not in chunk_map
        ):

            chunk_map[
                chunk.node_id
            ] = chunk

    ranked_ids = sorted(
        scores,
        key=scores.get,
        reverse=True
    )

    return [
        chunk_map[node_id]
        for node_id
        in ranked_ids
    ]