from src.vectorstore.chroma_client import collection


def save_chunk(
        chunk_id,
        text,
        metadata,
        embedding
):

    collection.add(
        ids=[chunk_id],
        documents=[text],
        metadatas=[metadata],
        embeddings=[embedding]
    )