from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from groq import Groq
import io
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Create FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(io.BytesIO(pdf_file))

    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text

# Home route
@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer Backend Running"
    }

# Analyze route
@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    try:

        # Read uploaded PDF
        pdf_content = await resume.read()

        # Extract text
        resume_text = extract_text_from_pdf(pdf_content)

        # Prompt
        prompt = f"""
        Analyze this resume against the job description.

        Resume:
        {resume_text}

        Job Description:
        {job_description}

        Give:
        1. ATS Score out of 100
        2. Matching Skills
        3. Missing Skills
        4. Strengths
        5. Improvement Suggestions
        """

        # Groq API call
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=1024
        )

        analysis = completion.choices[0].message.content

        return {
            "analysis": analysis
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "error": str(e)
        }