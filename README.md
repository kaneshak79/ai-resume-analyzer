# AI Resume Analyzer Backend

FastAPI backend for the AI Resume Analyzer application.  
This backend accepts resume PDFs and job descriptions, extracts resume content, and uses Groq LLM to generate ATS-style resume analysis.

---

## Features

- Upload Resume PDF
- Extract text from PDF
- Analyze resume against job description
- ATS Score generation
- Matching Skills detection
- Missing Skills suggestions
- AI-powered improvement recommendations
- FastAPI REST API
- CORS enabled for frontend integration

---

## Tech Stack

- FastAPI
- Groq API
- Python
- PyPDF2
- Uvicorn

---

## Project Structure

```bash
backend/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
