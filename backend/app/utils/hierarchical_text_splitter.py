from uuid import uuid4
from app.config.constants import (
    AUTO_MERGING_LEVEL_SIZES
)
from app.schemas.hierarchy_node import (
    HierarchyNode
)

def split_into_chunks(
    text: str,
    chunk_size: int
) -> list[str]:

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(
            text[start:end]
        )

        start += chunk_size

    return chunks

def build_hierarchy(
    text: str,
    document_id: str
) -> list[HierarchyNode]:

    all_nodes = []

    root_node = HierarchyNode(
        node_id=str(uuid4()),
        parent_id=None,
        level=-1,
        text=text,
        document_id=document_id
    )

    current_level_nodes = [root_node]

    for level, chunk_size in enumerate(
        AUTO_MERGING_LEVEL_SIZES
    ):

        next_level_nodes = []

        for parent_node in current_level_nodes:

            chunks = split_into_chunks(
                text=parent_node.text,
                chunk_size=chunk_size
            )

            for chunk in chunks:

                node = HierarchyNode(
                    node_id=str(uuid4()),
                    parent_id=parent_node.node_id,
                    level=level,
                    text=chunk,
                    document_id=document_id
                )

                all_nodes.append(node)
                next_level_nodes.append(node)

        current_level_nodes = next_level_nodes

        children_count_map = {}

    for node in all_nodes:

        children_count_map[
            node.parent_id
        ] = (
            children_count_map.get(
                node.parent_id,
                0
            ) + 1
        )

    for node in all_nodes:

        node.children_count = (
            children_count_map.get(
                node.node_id,
                0
            )
        )

    return all_nodes