from fastapi import APIRouter
from pathlib import Path

from app.schemas.request import AskRequest
from app.schemas.response import AskResponse
from app.services.rag_service import RagService
from app.schemas.retrieval_debug_response import (
    RetrievalDebugResponse
)

from app.retrieval.retriever import (
    retrieve_vector_context
)
from app.retrieval.bm25_retriever import (
    BM25Retriever
)
from app.retrieval.hybrid_retriever import HybridRetriever
from app.retrieval.multi_query_retriever import (
    MultiQueryRetriever
)
from app.schemas.filter_debug_request import (
    FilterDebugRequest
)
from app.retrieval.retriever import (
    retrieve_vector_context
)
from app.retrieval.sentence_window_retriever import (
    SentenceWindowRetriever
)
from app.schemas.retrieved_chunk import (
    RetrievedChunk
)
from app.utils.hierarchical_text_splitter import (
    build_hierarchy
)
from app.document_loaders.document_loader import (
    load_document
)
from app.vectorstore.system_design_collection import (
    get_collection
)
from app.retrieval.auto_merging_retriever import (
    AutoMergingRetriever
)
from app.vectorstore.system_design_collection import (
    get_collection
)
from app.retrieval.auto_merging_retriever import (
    AutoMergingRetriever
)
from app.retrieval.retriever import (
    retrieve_vector_context
)

multi_query_retriever = MultiQueryRetriever()
window_retriever = SentenceWindowRetriever()
bm25_retriever = BM25Retriever()
hybrid_retriever = HybridRetriever()

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

rag_service = RagService()


@router.post(
    "/ask",
    response_model=AskResponse
)
def ask(request: AskRequest):

    rag_response = rag_service.ask(
        request.question
    )

    return AskResponse(
        question=request.question,
        answer=rag_response.answer,
        sources=rag_response.sources,
        retrieved_chunks=rag_response.retrieved_chunks
    )

@router.post(
    "/debug",
    response_model=RetrievalDebugResponse
)
def debug_retrieval(
    request: AskRequest
):

    chunks = retrieve_vector_context(
        request.question
    )

    return RetrievalDebugResponse(
        question=request.question,
        retrieved_chunks=chunks
    )

@router.post("/bm25-debug")
def bm25_debug(
    request: AskRequest
):

    return bm25_retriever.retrieve(
        request.question
    )

@router.post("/hybrid-debug")
def hybrid_debug(
    request: AskRequest
):

    return hybrid_retriever.retrieve(
        request.question
    )

@router.post("/multi-query-debug")
def multi_query_debug(
    request: AskRequest
):
    return multi_query_retriever.retrieve(
        request.question
    )

@router.post("/filter-debug")
def filter_debug(
    request: FilterDebugRequest
):

    return retrieve_vector_context(
        query=request.question,
        document_id=request.document_id
    )

@router.get("/window-debug")
def window_debug():

    chunk = RetrievedChunk(
        content="",
        source="L4akshayResume.pdf",
        chunk_number=1,
        distance=0
    )

    return window_retriever.retrieve_window(
        chunk=chunk,
        window_size=1
    )

@router.get("/hierarchy-debug")
def hierarchy_debug():

    content = load_document(
        Path("data/sample_resume.pdf")
    )

    nodes = build_hierarchy(
        text=content,
        document_id="test"
    )

    return [
        {
            "node_id": node.node_id,
            "parent_id": node.parent_id,
            "level": node.level,
            "text_length": len(node.text)
        }
        for node in nodes
    ]

@router.get("/hierarchy-storage-debug")
def hierarchy_storage_debug():

    collection = get_collection()

    results = collection.get(
        include=[
            "documents",
            "metadatas"
        ]
    )

    return results["metadatas"][:20]

@router.get("/parent-debug")
def parent_debug():

    collection = get_collection()

    results = collection.get(
        include=["metadatas"]
    )

    node = None

    for metadata, node_id in zip(
        results["metadatas"],
        results["ids"]
    ):

        if metadata["level"] == 3:

            node = {
                "node_id": node_id,
                "parent_id": metadata["parent_id"]
            }

            break

    return node

@router.get("/parent-chain-debug")
def parent_chain_debug():

    collection = get_collection()

    results = collection.get(
        include=["metadatas"]
    )

    target_node = None

    for metadata, node_id in zip(
        results["metadatas"],
        results["ids"]
    ):

        if metadata["level"] == 3:

            target_node = node_id
            break

    if target_node is None:

        return {
            "error": "No level 3 node found"
        }

    retriever = AutoMergingRetriever()

    chain = retriever.get_parent_chain(
        target_node
    )

    return [
        {
            "id": node["id"],
            "level": node["metadata"]["level"],
            "parent_id": node["metadata"]["parent_id"]
        }
        for node in chain
    ]

@router.post(
    "/auto-merge-debug"
)
def auto_merge_debug(
    request: AskRequest
):

    chunks = retrieve_vector_context(
        request.question
    )

    retriever = (
        AutoMergingRetriever()
    )

    merged_chunks = (
        retriever.auto_merge(
            chunks
        )
    )

    return {
        "before_merge": [
            {
                "node_id": chunk.node_id,
                "parent_id": chunk.parent_id,
                "level": chunk.level
            }
            for chunk in chunks
        ],
        "after_merge": [
            {
                "node_id": chunk.node_id,
                "parent_id": chunk.parent_id,
                "level": chunk.level
            }
            for chunk in merged_chunks
        ]
    }



