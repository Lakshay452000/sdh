from pathlib import Path

from pypdf import PdfReader

from app.services.chroma_service import get_collection
from app.services.text_chunker import chunk_text

pdf_path = Path("data") / "sample_resume.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text

chunks = chunk_text(text)

collection = get_collection()

collection.add(
    ids=[f"resume_chunk_{i}" for i in range(len(chunks))],
    documents=chunks,
)

print(f"Stored {len(chunks)} chunks")
print(f"Collection count: {collection.count()}")