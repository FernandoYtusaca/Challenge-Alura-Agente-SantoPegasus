import streamlit as st

st.title(
    "Santo Pegasus RAG"
)

question = st.chat_input(
    "Haz una pregunta"
)

if question:

    st.chat_message(
        "user"
    ).write(question)

    answer = "Respuesta"

    st.chat_message(
        "assistant"
    ).write(answer)