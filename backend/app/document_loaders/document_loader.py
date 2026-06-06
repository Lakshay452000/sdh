from pathlib import Path

from app.document_loaders.pdf_loader import load_pdf


def load_document(file_path: Path) -> str:

    suffix = file_path.suffix.lower()

    if suffix == ".txt":
        return file_path.read_text(
            encoding="utf-8"
        )

    if suffix == ".pdf":
        return load_pdf(
            str(file_path)
        )

    raise ValueError(
        f"Unsupported file type: {suffix}"
    )