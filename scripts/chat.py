from src.rag.generator import generate_answer

print("Asistente RAG Corporativo")
print("Escribe 'salir' para terminar")

while True:

    question = input("\nPregunta: ")

    if question.lower() == "salir":
        break

    answer = generate_answer(question)

    print("\nRespuesta:")
    print(answer)