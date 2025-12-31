import pdfplumber
import pytesseract
from PIL import Image

def extract_text_from_pdf(file_obj):
    text = ""
    with pdfplumber.open(file_obj) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_image(file_obj):
    image = Image.open(file_obj)
    return pytesseract.image_to_string(image)