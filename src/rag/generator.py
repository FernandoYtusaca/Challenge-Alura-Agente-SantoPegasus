from langchain_ollama import ChatOllama

from src.rag.retriever import search_documents


llm = ChatOllama(
    model="llama3.1",
    temperature=0
)


def generate_answer(question):

    documents = search_documents(question)

    context = "\n\n".join(
        [
            doc["text"]
            for doc in documents
        ]
    )

    prompt = f"""
Eres un asistente técnico corporativo.

Responde únicamente utilizando la información
proporcionada en el contexto.

Si la respuesta no aparece en el contexto,
indica claramente que no existe suficiente
información disponible.

CONTEXTO:
{context}

PREGUNTA:
{question}
"""

    response = llm.invoke(prompt)

    return response.content