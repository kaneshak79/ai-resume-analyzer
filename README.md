# AI Resume Analyzer Backend

AI-powered Resume Analyzer backend built using FastAPI and Groq LLM.  
This backend accepts resume PDFs and job descriptions, extracts resume text, and generates ATS-style analysis including ATS score, matching skills, missing skills, strengths, and improvement suggestions.

---

# Features

- Resume PDF Upload
- Resume Text Extraction
- AI ATS Resume Analysis
- Matching Skills Detection
- Missing Skills Suggestions
- Resume Improvement Recommendations
- FastAPI REST API
- Groq LLM Integration
- CORS Enabled for Frontend Communication

---

# Tech Stack

- FastAPI
- Python
- Groq API
- PyPDF2
- Uvicorn

---

# Project Structure

```bash
backend/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/ai-resume-analyzer-backend.git
```

## Navigate to Backend Folder

```bash
cd backend
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in backend folder:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Run Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```txt
http://127.0.0.1:8000
```

---

# API Endpoints

## Home Route

### Request

```http
GET /
```

### Response

```json
{
  "message": "AI Resume Analyzer Backend Running"
}
```

---

## Analyze Resume

### Request

```http
POST /analyze
```

### Form Data

| Field | Type |
|---|---|
| resume | PDF File |
| job_description | String |

---

# Example Response

```json
{
  "analysis": "ATS Score: 85/100\nMatching Skills: ..."
}
```

---

# CORS Configuration

CORS is enabled for frontend integration.

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

# Deployment

## Deploy Backend on Render

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

# Environment Variables on Render

Add:

| KEY | VALUE |
|---|---|
| GROQ_API_KEY | your_actual_api_key |

---

# Frontend

Frontend built using React.js.

---

# Author

Kanesha

```
