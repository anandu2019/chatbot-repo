from fastapi import FastAPI, UploadFile, File, HTTPException
from ocr_utils import extract_text_from_pdf, extract_text_from_image
from openai_utils import parse_resume_with_hf
from schema import ResumeResponse
from fastapi.middleware.cors import CORSMiddleware

import openai
import os  
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("HF_API_TOKEN")

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/upload", response_model=ResumeResponse)
async def upload_resume(file: UploadFile = File(...)):
    text = ""

    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file.file)
    elif file.filename.lower().endswith((".jpg", ".jpeg", ".png")):
        text = extract_text_from_image(file.file)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    if not text.strip():
        raise HTTPException(status_code=422, detail="Could not extract text from file")

    resume_data = parse_resume_with_hf(text)
    return ResumeResponse(**resume_data)
