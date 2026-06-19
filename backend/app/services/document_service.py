from pathlib import Path
from uuid import uuid4

from networkx import nodes

from app.document_loaders.document_loader import (
    load_document
)
from app.vectorstore.system_design_collection import (
    get_collection
)
from app.schemas.document_response import (
    DocumentResponse
)
from app.utils.hierarchical_text_splitter import (
    build_hierarchy
)


class DocumentService:

    def ingest_document(
        self,
        file_path: Path,
        original_file_name: str
    ) -> str:

        collection = get_collection()

        document_id = str(uuid4())

        content = load_document(file_path)

        if not content.strip():
            raise ValueError(
                "Document is empty"
            )
        
        nodes = build_hierarchy(
            text=content,
            document_id=document_id
        )

        documents = []
        ids = []
        metadatas = []

        for node in nodes:

            documents.append(
                node.text
            )

            ids.append(
                node.node_id
            )

            metadatas.append(
                {
                    "document_id": node.document_id,
                    "node_id": node.node_id,
                    "parent_id": (
                        node.parent_id
                        if node.parent_id is not None
                        else "ROOT"
                    ),
                    "level": node.level,
                    "children_count": node.children_count,
                    "chunk_type": "hierarchy",
                    "source": original_file_name,
                    "file_name": original_file_name
                }
            )

        collection.add(
            documents=documents,
            ids=ids,
            metadatas=metadatas
        )

        return document_id
    
    def list_documents(
        self
    ) -> list[DocumentResponse]:

        collection = get_collection()

        results = collection.get(
            include=["metadatas"]
        )

        unique_documents = {}

        for metadata in results["metadatas"]:

            document_id = metadata["document_id"]

            if document_id not in unique_documents:

                unique_documents[
                    document_id
                ] = DocumentResponse(
                    document_id=document_id,
                    file_name=metadata["file_name"]
                )

        return list(
            unique_documents.values()
        )

    def delete_document(
        self,
        document_id: str
    ) -> None:

        collection = get_collection()

        results = collection.get(
            where={
                "document_id": document_id
            }
        )

        ids = results["ids"]

        if not ids:
            raise ValueError(
                "Document not found"
            )

        collection.delete(
            ids=ids
        )

    def get_all_chunks(self):

        collection = get_collection()

        return collection.get(
            include=["documents", "metadatas"]
        )







