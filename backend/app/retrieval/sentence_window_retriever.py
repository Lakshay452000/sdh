from app.vectorstore.system_design_collection import (
    get_collection
)

from app.schemas.retrieved_chunk import (
    RetrievedChunk
)


class SentenceWindowRetriever:

    def retrieve_window(
        self,
        chunk: RetrievedChunk,
        window_size: int = 1
    ) -> list[RetrievedChunk]:

        collection = get_collection()

        document_id = None

        results = collection.get(
            where={
                "source": chunk.source
            },
            include=["documents", "metadatas"]
        )

        window_chunks = []

        for document, metadata in zip(
            results["documents"],
            results["metadatas"]
        ):

            current_chunk_number = (
                metadata["chunk_number"]
            )

            if (
                chunk.chunk_number - window_size
                <= current_chunk_number
                <= chunk.chunk_number + window_size
            ):

                window_chunks.append(
                    RetrievedChunk(
                        content=document,
                        source=metadata["source"],
                        chunk_number=current_chunk_number,
                        distance=0
                    )
                )

        window_chunks.sort(
            key=lambda c: c.chunk_number
        )

        return window_chunks