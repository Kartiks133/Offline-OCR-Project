# Secure Offline OCR PDF Converter

A fully offline OCR-based PDF to editable DOCX conversion system designed for privacy-sensitive environments such as PSU organizations, government offices, and secure internal networks.

This application converts scanned PDF documents into editable Microsoft Word (.docx) files without using any online APIs or cloud services.

---

# Features

- Fully Offline OCR Processing
- PDF to Editable DOCX Conversion
- Local File Processing
- No Cloud APIs
- No Internet Dependency
- Secure Document Handling
- Multi-page PDF Support
- Modern User Interface
- Automatic DOCX Download

---

# Problem Statement

Many OCR solutions available online require documents to be uploaded to cloud servers or third-party APIs. This creates security and privacy concerns for organizations handling confidential or sensitive documents.

This project solves that problem by ensuring:

- All processing occurs locally
- No data leaves the user's machine
- No external APIs are used
- No online OCR services are involved

---

# System Workflow

```text
Scanned PDF
      ↓
PDF Upload
      ↓
PDF to Image Conversion
      ↓
Tesseract OCR Extraction
      ↓
Text Processing
      ↓
DOCX Generation
      ↓
Editable Word File Download
```

---

# Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- FastAPI
- Python

## OCR Engine
- Tesseract OCR

## PDF Processing
- Poppler
- pdf2image

## Document Generation
- python-docx

---

# Project Architecture

```text
Frontend (HTML/CSS/JS)
            ↓
FastAPI Backend
            ↓
PDF Processing Engine
            ↓
Tesseract OCR Engine
            ↓
DOCX Generation
            ↓
Editable Word Output
```

---

# Folder Structure

```text
Offline-OCR-Project/
│
├── backend/
│   ├── main.py
│   ├── uploads/
│   ├── temp/
│   ├── outputs/
│   └── venv/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# Installation Guide

## 1. Clone Repository

```bash
git clone <repository-url>
```

---

## 2. Backend Setup

Move to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn python-multipart
pip install pdf2image
pip install pytesseract
pip install python-docx
```

---

# Required External Software

## Install Poppler

Download:
https://github.com/oschwartz10612/poppler-windows/releases/

Add Poppler `bin` folder to system PATH.

---

## Install Tesseract OCR

Download:
https://github.com/UB-Mannheim/tesseract/wiki

During installation:
- Enable "Add Tesseract to PATH"

---

# Running the Application

## Start Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

## Start Frontend

Open:

```text
frontend/index.html
```

in browser

OR

Use VS Code Live Server.

---

# Usage Instructions

1. Open application
2. Select scanned PDF
3. Click "Convert to DOCX"
4. Wait for OCR processing
5. Download editable Word document

---

# Security Advantages

- No online processing
- No cloud uploads
- No third-party OCR APIs
- No external document storage
- Suitable for confidential document handling

---

# Current Limitations

- Formatting preservation is limited
- Table reconstruction not implemented
- Handwriting OCR not supported
- Multi-column parsing not implemented
- OCR accuracy depends on scan quality

---

# Future Enhancements

- Better OCR preprocessing
- Noise reduction
- Table detection
- Layout reconstruction
- Multi-language OCR
- Drag-and-drop upload
- Progress tracking
- Dark mode UI

---

# Target Use Cases

- PSU Organizations
- Government Offices
- Legal Document Digitization
- Archived Record Conversion
- Internal Enterprise Document Processing
- Secure Offline Networks

---

# Author

Kartik Shrivastava

---

# License
This project is developed for educational and organizational use.

<img width="1918" height="1013" alt="image" src="https://github.com/user-attachments/assets/5f49a849-563b-4845-a05e-1b85c2734a6e" />

