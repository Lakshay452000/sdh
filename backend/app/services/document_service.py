from pathlib import Path
from uuid import uuid4

from app.document_loaders.document_loader import (
    load_document
)
from app.vectorstore.system_design_collection import (
    get_collection
)
from app.schemas.document_response import (
    DocumentResponse
)
from app.utils.text_splitter import split_text


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

        chunks = split_text(content)

        documents = []
        ids = []
        metadatas = []

        for index, chunk in enumerate(chunks):

            documents.append(chunk)

            ids.append(
                f"{document_id}_chunk_{index}"
            )

            metadatas.append(
                {
                    "document_id": document_id,
                    "source": original_file_name,
                    "file_name": original_file_name,
                    "chunk_number": index
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







