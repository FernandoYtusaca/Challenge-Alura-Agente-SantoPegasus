import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from src.rag.retriever import search_documents


question = "¿Qué tecnologías usa Santo Pegasus?"

results = search_documents(question)


for i, result in enumerate(results):
    print("\n--- RESULTADO", i + 1, "---")
    print(result["text"][:500])
    print(result["metadata"])