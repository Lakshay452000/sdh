from pypdf import PdfReader
from app.services.text_chunker import chunk_text
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

pdf_path = BASE_DIR / "data" / "sample_resume.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text

chunks = chunk_text(text)

print(f"Total characters: {len(text)}")
print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print(f"\n===== Chunk {i + 1} =====")
    print(chunk[:200])