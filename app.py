import streamlit as st

from src.rag.generator import generate_answer

st.set_page_config(
    page_title="Asistente RAG",
    page_icon="🤖"
)

st.title("🤖 Asistente RAG Corporativo")

question = st.text_input(
    "Haz una pregunta sobre la documentación"
)

if question:

    with st.spinner("Buscando respuesta..."):

        answer = generate_answer(question)

    st.markdown("### Respuesta")
    st.write(answer)