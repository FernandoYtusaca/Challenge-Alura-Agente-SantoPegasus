from src.vectorstore.chroma_client import collection
from src.rag.embeddings import create_embedding


def search_documents(query, k=5):
    """
    Busca los chunks más relevantes para una pregunta.
    """

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    return [
        {
            "text": doc,
            "metadata": meta
        }
        for doc, meta in zip(documents, metadatas)
    ]