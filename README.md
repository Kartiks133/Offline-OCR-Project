# Offline OCR + Local AI PDF Assistant

A fully offline and privacy-focused OCR + AI document assistant built using FastAPI, Tesseract OCR, FAISS, Sentence Transformers, Ollama, and Phi-3.

This project extracts text from scanned PDFs, converts them into searchable semantic embeddings, and allows users to chat with documents locally — without using any cloud APIs.

---

# Features

- Offline OCR PDF processing
- Local AI-powered PDF chat
- Semantic document search
- FAISS vector retrieval
- Local LLM integration using Ollama
- Privacy-first architecture
- No OpenAI or cloud dependency
- FastAPI backend
- Interactive frontend UI

---

# Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- FastAPI
- Python

## OCR
- Tesseract OCR
- pdf2image

## AI / NLP
- Sentence Transformers
- FAISS
- Ollama
- Phi-3

---

# Project Architecture

```text
PDF Upload
    ↓
OCR Extraction
    ↓
Structured JSON Storage
    ↓
Chunking
    ↓
Embeddings
    ↓
FAISS Vector Search
    ↓
Local LLM (Phi-3)
    ↓
AI Response
```

---

# Folder Structure

```text
Offline-OCR-Project/
│
├── backend/
│   ├── retrieval/
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   ├── generate_answer.py
│   │   ├── metadata_store.py
│   │   ├── search.py
│   │   └── vector_store.py
│   │
│   ├── extracted_text/
│   ├── uploads/
│   ├── outputs/
│   ├── temp/
│   ├── main.py
│   └── test_retrieval.py
│
├── frontend/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Kartiks133/Offline-OCR-Project.git
```

```bash
cd Offline-OCR-Project
```

---

# 2. Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4. Install Tesseract OCR

Download:
https://github.com/UB-Mannheim/tesseract/wiki

After installation, update this path inside `backend/main.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

# 5. Install Ollama

Download:
https://ollama.com/

---

# 6. Pull Phi-3 Model

```bash
ollama run phi3
```

This downloads the local AI model.

After first download, everything works fully offline.

---

# Running The Project

## Start Backend

```bash
cd backend
```

```bash
uvicorn main:app --reload
```

---

## Open Frontend

Open the frontend HTML file in browser.

---

# API Endpoints

## Convert PDF

```http
POST /convert
```

Converts scanned PDFs into searchable OCR text and DOCX.

---

## Chat With PDF

```http
POST /chat
```

### Request

```json
{
    "question": "What is this document about?"
}
```

### Response

```json
{
    "answer": "The document discusses..."
}
```

---

# Privacy & Security

This project is completely offline after initial setup.

No files, embeddings, prompts, or document data are sent to:
- OpenAI
- Google APIs
- Cloud services
- External servers

Suitable for:
- confidential documents
- enterprise environments
- research labs
- government workflows
- privacy-sensitive processing

---

# Future Improvements

- Persistent FAISS indexing
- Source citations with page numbers
- Multi-document chat
- Chat history
- OCR preprocessing improvements
- Dark mode UI
- Streaming responses
- Encrypted local storage

---

# Screenshots

<img width="1919" height="1015" alt="image" src="https://github.com/user-attachments/assets/ed12ca1c-4a9a-4c9b-8aaa-1efe84238cd3" />
<img width="1607" height="363" alt="image" src="https://github.com/user-attachments/assets/f67e345e-0793-4e6b-b52b-a060c5d1d8fe" />



# Architecture Diagram

PDF
 ↓
OCR
 ↓
Embeddings
 ↓
FAISS
 ↓
Phi-3
 ↓
AI Answer

---

# Author

Kartik Shrivastava

GitHub:
https://github.com/Kartiks133

---
