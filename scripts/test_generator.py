from src.rag.generator import generate_answer


question = "¿Cuál es la política de privilegio mínimo?"

answer = generate_answer(question)

print("\nRESPUESTA:")
print(answer)