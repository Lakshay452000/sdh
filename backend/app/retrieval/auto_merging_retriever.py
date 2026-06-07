from app.vectorstore.system_design_collection import (
    get_collection
)
from collections import defaultdict
from app.schemas.retrieved_chunk import (
    RetrievedChunk
)
from app.config.constants import (
    AUTO_MERGE_THRESHOLD
)

class AutoMergingRetriever:

    def __init__(self):

        self.collection = get_collection()

    def get_parent(
        self,
        parent_id: str
    ):

        results = self.collection.get(
            ids=[parent_id],
            include=["documents", "metadatas"]
        )

        if not results["ids"]:
            return None

        return {
            "id": results["ids"][0],
            "content": results["documents"][0],
            "metadata": results["metadatas"][0]
        }
    
    def get_node(
        self,
        node_id: str
    ):

        results = self.collection.get(
            ids=[node_id],
            include=["documents", "metadatas"]
        )

        if not results["ids"]:
            return None

        return {
            "id": results["ids"][0],
            "content": results["documents"][0],
            "metadata": results["metadatas"][0]
        }

    def get_parent_chain(
        self,
        node_id: str
    ):

        chain = []

        current = self.get_node(
            node_id
        )

        while current:

            chain.append(
                current
            )

            parent_id = current[
                "metadata"
            ][
                "parent_id"
            ]

            if parent_id == "ROOT":
                break

            current = self.get_node(
                parent_id
            )

        return chain

    def merge_once(
        self,
        chunks: list[RetrievedChunk]
    ) -> tuple[
        list[RetrievedChunk],
        bool
    ]:

        # print("\nINPUT TO MERGE")

        # for chunk in chunks:

        #     print(
        #         f"node={chunk.node_id[:8]} "
        #         f"parent={chunk.parent_id[:8]} "
        #         f"level={chunk.level}"
        #     )

        parent_groups = defaultdict(list)

        for chunk in chunks:

            parent_groups[
                chunk.parent_id
            ].append(chunk)

        # print("\nGROUPS")

        # for parent_id, siblings in (
        #     parent_groups.items()
        # ):

        #     print(
        #         f"parent={parent_id[:8]}"
        #     )

        #     for chunk in siblings:

        #         print(
        #             f"   child={chunk.node_id[:8]}"
        #         )

        merged_chunks = []
        merge_happened = False

        for parent_id, siblings in (
            parent_groups.items()
        ):

            parent_node = self.get_node(
                parent_id
            )

            if parent_node is None:

                merged_chunks.extend(
                    siblings
                )

                continue

            retrieved_children = (
                len(siblings)
            )

            total_children = (
                parent_node[
                    "metadata"
                ][
                    "children_count"
                ]
            )

            coverage = (
                retrieved_children /
                total_children
                if total_children > 0
                else 0
            )

            # print(
            #     f"\nparent={parent_id[:8]} "
            #     f"retrieved={retrieved_children} "
            #     f"total={total_children} "
            #     f"coverage={coverage:.2f}"
            # )

            if (
                total_children > 1
                and
                coverage >= AUTO_MERGE_THRESHOLD
            ):

                reranker_scores = [
                    chunk.reranker_score
                    for chunk in siblings
                    if chunk.reranker_score is not None
                ]

                bm25_scores = [
                    chunk.bm25_score
                    for chunk in siblings
                    if chunk.bm25_score is not None
                ]

                # print(
                #     f"MERGING -> {parent_id[:8]}"
                # )

                merged_chunks.append(
                    RetrievedChunk(
                        content=parent_node[
                            "content"
                        ],
                        source=siblings[0].source,
                        node_id=parent_node[
                            "id"
                        ],
                        parent_id=parent_node[
                            "metadata"
                        ][
                            "parent_id"
                        ],
                        level=parent_node[
                            "metadata"
                        ][
                            "level"
                        ],
                        distance=min(
                            chunk.distance
                            for chunk in siblings
                        ),
                        reranker_score=(
                            max(reranker_scores)
                            if reranker_scores
                            else None
                        ),
                        bm25_score=(
                            max(bm25_scores)
                            if bm25_scores
                            else None
                        )
                    )
                )

                merge_happened = True

            else:

                # print(
                #     f"KEEPING CHILDREN OF {parent_id[:8]}"
                # )

                merged_chunks.extend(
                    siblings
                )

        # print("\nMERGED RESULT")

        # for chunk in merged_chunks:

        #     print(
        #         f"node={chunk.node_id[:8]} "
        #         f"level={chunk.level}"
        #     )

        return (
            merged_chunks,
            merge_happened
        )

    def auto_merge(
        self,
        chunks: list[RetrievedChunk]
    ) -> list[RetrievedChunk]:

        current_chunks = chunks

        while True:

            (
                merged_chunks,
                merge_happened
            ) = self.merge_once(
                current_chunks
            )

            if not merge_happened:
                break

            current_chunks = (
                merged_chunks
            )

        return current_chunks
