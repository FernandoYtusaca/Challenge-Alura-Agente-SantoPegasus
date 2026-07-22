import streamlit as st

documento = st.selectbox(
    "Documento",
    [
        "Todos",
        "backend",
        "frontend",
        "arquitectura",
        "onboarding",
        "incidentes"
    ]
)

pagina = st.number_input(
    "Página",
    min_value=1
)