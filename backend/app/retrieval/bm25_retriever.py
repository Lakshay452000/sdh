from rank_bm25 import BM25Okapi

from app.vectorstore.system_design_collection import (
    get_collection
)

from app.schemas.retrieved_chunk import (
    RetrievedChunk
)

from app.config.constants import (
    AUTO_MERGING_LEVEL_SIZES
)

from app.schemas.metadata_filter import (
    MetadataFilter
)

leaf_level = (
    len(AUTO_MERGING_LEVEL_SIZES) - 1
)


class BM25Retriever:

    def __init__(self):

        self.collection = (
            get_collection()
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 10,
        metadata_filter: MetadataFilter | None = None
    ) -> list[RetrievedChunk]:

        results = self.collection.get(
            include=[
                "documents",
                "metadatas"
            ]
        )

        documents = results[
            "documents"
        ]

        metadatas = results[
            "metadatas"
        ]

        leaf_documents = []

        leaf_metadatas = []

        for document, metadata in zip(
            documents,
            metadatas
        ):

            if (
                metadata["level"]
                !=
                leaf_level
            ):
                continue

            if metadata_filter:

                if (
                    metadata_filter.document_id
                    and
                    metadata["document_id"]
                    !=
                    metadata_filter.document_id
                ):
                    continue

                if (
                    metadata_filter.file_name
                    and
                    metadata["file_name"]
                    !=
                    metadata_filter.file_name
                ):
                    continue

                if (
                    metadata_filter.chunk_type
                    and
                    metadata["chunk_type"]
                    !=
                    metadata_filter.chunk_type
                ):
                    continue

                if (
                    metadata_filter.level is not None
                    and
                    metadata["level"]
                    !=
                    metadata_filter.level
                ):
                    continue

            leaf_documents.append(
                document
            )

            leaf_metadatas.append(
                metadata
            )
        if not leaf_documents:
            return []
        
        tokenized_documents = [

            document
            .lower()
            .split()

            for document
            in leaf_documents
        ]

        bm25 = BM25Okapi(
            tokenized_documents
        )

        scores = bm25.get_scores(
            query
            .lower()
            .split()
        )

        scored_documents = list(
            zip(
                leaf_documents,
                leaf_metadatas,
                scores
            )
        )

        scored_documents.sort(
            key=lambda item: item[2],
            reverse=True
        )

        chunks = []

        for (
            document,
            metadata,
            score
        ) in scored_documents[:top_k]:

            chunks.append(
                RetrievedChunk(
                    content=document,
                    source=metadata[
                        "source"
                    ],
                    node_id=metadata[
                        "node_id"
                    ],
                    parent_id=metadata[
                        "parent_id"
                    ],
                    level=metadata[
                        "level"
                    ],
                    distance=0.0,
                    bm25_score=float(
                        score
                    )
                )
            )

        return chunks