# app/tests/test_retrieval.py

from app.services.chroma_service import get_collection

collection = get_collection()

results = collection.query(
    query_texts=["What technologies does Lakshay know?"],
    n_results=3
)

print(results["documents"])