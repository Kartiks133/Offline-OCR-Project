from fastapi import FastAPI, UploadFile, File
import os
import uuid
from pdf2image import convert_from_path
import pytesseract  
from docx import Document
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Folder where uploaded PDFs will be stored
UPLOAD_DIR = "uploads"
TEMP_DIR = "temp"
OUTPUT_DIR = "outputs"

# Create uploads folder automatically if missing
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Backend Working"}


@app.post("/convert")
async def convert_pdf(file: UploadFile = File(...)):

    # Validate file type
    if file.content_type != "application/pdf":
        return {"error": "Only PDF files are allowed"}

    # Generate unique filename
    unique_filename = f"{uuid.uuid4()}.pdf"

    # Full path where file will be saved
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    pages=convert_from_path(file_path)
    saved_images= []
    extracted_text=""

    for index, page in enumerate(pages):
        image_name=f"page_{index+1}.jpg"
        image_path=os.path.join(TEMP_DIR,image_name)
        page.save(image_path,"JPEG")
        saved_images.append(image_name)
        text= pytesseract.image_to_string(page)
        extracted_text+=text+"\n\n"
    
    document= Document()
    document.add_paragraph(extracted_text)
    output_fileame=f"{uuid.uuid4()}.docx"
    output_path= os.path.join(OUTPUT_DIR,output_fileame)
    document.save(output_path)

    return FileResponse(
        output_path,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename="converted.docx"
        )