import json
from fastapi import FastAPI, UploadFile, File
import os
import uuid
from pdf2image import convert_from_path
import pytesseract
from docx import Document
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from retrieval.chunker import chunk_text
from retrieval.embedder import generate_embeddings
from retrieval.embedder import model
from retrieval.vector_store import VectorStore
from retrieval.generate_answer import generate_answer


app = FastAPI()
class ChatRequest(BaseModel):
    question: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Folder paths
UPLOAD_DIR = "uploads"
TEMP_DIR = "temp"
OUTPUT_DIR = "outputs"
EXTRACTED_TEXT_DIR = "extracted_text"

# Create folders automatically
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(EXTRACTED_TEXT_DIR, exist_ok=True)

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


@app.get("/")
def home():
    return {"message": "Backend Working"}


@app.post("/convert")
async def convert_pdf(file: UploadFile = File(...)):

    # Validate PDF
    if file.content_type != "application/pdf":
        return {"error": "Only PDF files are allowed"}

    # Generate unique PDF filename
    unique_filename = f"{uuid.uuid4()}.pdf"

    # Save uploaded PDF
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Convert PDF pages to images
    pages = convert_from_path(file_path)

    saved_images = []
    extracted_text = ""

    # JSON structure for future AI search
    document_data = {
        "document": unique_filename,
        "pages": []
    }

    # OCR processing
    for index, page in enumerate(pages):

        image_name = f"page_{index + 1}.jpg"

        image_path = os.path.join(TEMP_DIR, image_name)

        page.save(image_path, "JPEG")

        saved_images.append(image_name)

        # OCR
        text = pytesseract.image_to_string(page)

        # Store page text in JSON structure
        document_data["pages"].append({
            "page": index + 1,
            "text": text
        })

        # Full extracted text
        extracted_text += text + "\n\n"

    # Save extracted text JSON
    json_filename = f"{uuid.uuid4()}.json"

    json_path = os.path.join(
        EXTRACTED_TEXT_DIR,
        json_filename
    )

    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(document_data, json_file, indent=4)

    # Generate DOCX
    document = Document()

    document.add_paragraph(extracted_text)

    output_filename = f"{uuid.uuid4()}.docx"

    output_path = os.path.join(
        OUTPUT_DIR,
        output_filename
    )

    document.save(output_path)

    # Return DOCX file
    return FileResponse(
        output_path,
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "wordprocessingml.document"
        ),
        filename="converted.docx"
    )
@app.post("/chat")
async def chat(request: ChatRequest):

    json_folder = "extracted_text"

    json_files = os.listdir(json_folder)

    if not json_files:
        return {"answer": "No documents found."}

    latest_json = os.path.join(
        json_folder,
        json_files[-1]
    )

    # LOAD JSON
    with open(latest_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    # COMBINE TEXT
    full_text = ""

    for page in data["pages"]:
        full_text += page["text"] + "\n"

    # CHUNKING
    chunks = chunk_text(full_text)

    # EMBEDDINGS
    embeddings = generate_embeddings(chunks)

    # VECTOR STORE
    dimension = embeddings.shape[1]

    store = VectorStore(dimension)

    store.add_embeddings(embeddings)

    # QUESTION
    query = request.question

    query_embedding = model.encode(query)

    distances, indices = store.search(query_embedding)

    # BUILD CONTEXT
    context = ""

    for idx in indices[0]:
        context += chunks[idx] + "\n"

    # AI ANSWER
    answer = generate_answer(
        query,
        context
    )

    return {
        "answer": answer
    }