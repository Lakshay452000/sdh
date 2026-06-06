from app.document_loaders.pdf_loader import load_pdf

content = load_pdf(
    "data/sample_resume.pdf"
)

print(content[:1000])