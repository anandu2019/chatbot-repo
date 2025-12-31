import json, re
from transformers import pipeline

# Load the model once at startup
nlp = pipeline("text2text-generation", model="google/flan-t5-base")

def clean_output(raw: str):
    """
    Extracts the first valid JSON object from a raw model output string.
    """
    matches = re.findall(r"\{.*?\}", raw, re.DOTALL)
    for candidate in matches:
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            continue
    return {"error": "No valid JSON found"}

def parse_resume_with_hf(text: str):
    """
    Calls Hugging Face locally via transformers and returns cleaned JSON.
    """
    prompt = f"""
    Extract the following fields from this resume text and return valid JSON only:

    {{
      "Name": "",
      "Email": "",
      "Phone Number": "",
      "Skills": [],
      "Years of Experience": "",
      "Education": "",
      "Current/Last Job": "",
      "Companies Worked At": [],
      "LinkedIn": "",
      "Certifications": [],
      "Location": ""
    }}

    Resume text: {text}
    """

    result = nlp(prompt, max_length=512)
    raw_output = result[0]["generated_text"]

    return clean_output(raw_output)