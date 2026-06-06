from fastapi import APIRouter

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







