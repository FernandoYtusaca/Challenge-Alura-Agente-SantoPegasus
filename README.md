# 🤖 Asistente RAG Corporativo

Asistente de preguntas y respuestas basado en la arquitectura **Retrieval-Augmented Generation (RAG)**, desarrollado para consultar documentación corporativa mediante lenguaje natural.

El sistema procesa documentos PDF, genera embeddings semánticos, almacena la información en una base vectorial y utiliza un modelo de lenguaje para responder preguntas basándose únicamente en el contenido de los documentos indexados.

---

# 📋 Características

* Carga automática de documentos PDF.
* División inteligente de documentos en fragmentos (chunks).
* Generación de embeddings mediante modelos de Sentence Transformers.
* Almacenamiento vectorial utilizando ChromaDB.
* Recuperación semántica de información relevante.
* Generación de respuestas mediante Ollama y modelos locales.
* Interfaz de línea de comandos.
* Interfaz web desarrollada con Streamlit.
* Arquitectura modular y escalable.

---

# 🏗️ Arquitectura

```text
Documentos PDF
        │
        ▼
Carga de documentos
        │
        ▼
Chunking
        │
        ▼
Embeddings (BGE)
        │
        ▼
ChromaDB
        │
        ▼
Retriever
        │
        ▼
Ollama (LLM)
        │
        ▼
Respuesta al usuario
```

---

# 🛠️ Tecnologías Utilizadas

## Backend

* Python 3.12+
* ChromaDB
* Sentence Transformers
* Ollama
* Streamlit

## Modelos

### Embeddings

```text
BAAI/bge-small-en-v1.5
```

### Modelo Generativo

Ejemplo:

```text
llama3.1
```

También es compatible con:

```text
mistral
```

---

# 📁 Estructura del Proyecto

```text
Poyecto/
│
├── data/
│   └── documents/
│
├── scripts/
│   ├── ingest.py
│   ├── test_retriever.py
│   ├── test_generator.py
│   └── chat.py
│
├── src/
│   ├── ingestion/
│   │   ├── pdf_loader.py
│   │   ├── chunker.py
│   │   ├── metadata_extractor.py
│   │   └── indexer.py
│   │
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   └── generator.py
│   │
│   └── vectorstore/
│       └── chroma_client.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Instalación

## 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Poyecto
```

## 2. Crear entorno virtual

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 🦙 Configuración de Ollama

Instalar Ollama:

```bash
https://ollama.com/download
```

Descargar un modelo:

```bash
ollama pull llama3.1
```

Verificar instalación:

```bash
ollama list
```

---

# 📥 Ingestión de Documentos

Colocar los documentos PDF dentro de la carpeta correspondiente.

Ejecutar:

```bash
python scripts/ingest.py
```

Salida esperada:

```text
Páginas cargadas: 152
Chunks creados: 596
Indexación completada
```

---

# 🔎 Prueba del Retriever

```bash
python -m scripts.test_retriever
```

Esta prueba permite verificar que el sistema recupera los fragmentos más relevantes para una consulta.

---

# 🧠 Prueba del Generador

```bash
python -m scripts.test_generator
```

Permite validar la integración entre el Retriever y el modelo de lenguaje.

---

# 💬 Uso desde Consola

```bash
python -m scripts.chat
```

Ejemplo:

```text
Pregunta:
¿Cómo funciona el proceso de onboarding?

Respuesta:
[Respuesta generada por el sistema]
```

---

# 🌐 Uso con Streamlit

Iniciar la aplicación web:

```bash
streamlit run app.py
```

Abrir en el navegador:

```text
http://localhost:8501
```

---

# 🔄 Flujo RAG

## 1. Indexación

* Lectura de documentos PDF.
* División en chunks.
* Generación de embeddings.
* Almacenamiento en ChromaDB.

## 2. Consulta

* El usuario realiza una pregunta.
* Se genera un embedding de la consulta.
* ChromaDB recupera los fragmentos más relevantes.
* El modelo local genera una respuesta basada en el contexto recuperado.

---

# 🚀 Posibles Mejoras Futuras

* Memoria conversacional.
* Citas automáticas de fuentes.
* Historial de conversaciones.
* Soporte para múltiples formatos de documentos.
* Despliegue en la nube.
* Panel administrativo.
* Evaluación automática de respuestas.
* Autenticación y control de acceso.

---

# 👨‍💻 Autor

**Saúl Fernando Ytusaca Quispe**

Proyecto desarrollado como parte del Challenge de IA y RAG.

---

# 📄 Licencia

Este proyecto se distribuye con fines educativos y de aprendizaje.
