import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

from src.ingestion.pdf_loader import load_pdf
from src.ingestion.chunker import split_documents
from src.ingestion.metadata_extractor import (
    detect_document,
    detect_section
)

from src.ingestion.indexer import save_chunk
from src.rag.embeddings import create_embedding

docs = load_pdf(
    "data/raw/Alura documentacion challenge.pdf"
)

print(f"Páginas cargadas: {len(docs)}")

chunks = split_documents(docs)

print(f"Chunks creados: {len(chunks)}")

for idx, chunk in enumerate(chunks):

    text = chunk.page_content

    page = chunk.metadata.get(
        "page",
        0
    )

    metadata = {
        "documento": detect_document(text),
        "seccion": detect_section(text),
        "pagina": page
    }

    embedding = create_embedding(text)

    save_chunk(
        chunk_id=f"chunk_{idx}",
        text=text,
        metadata=metadata,
        embedding=embedding
    )

print("Indexación completada")