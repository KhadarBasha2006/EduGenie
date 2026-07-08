# 🧠✨ EduGenie – AI-Powered Learning Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/MBZUAI/LaMini-Flan-T5-783M)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**EduGenie** is a lightweight, intelligent educational assistant powered by **Google Gemini 2.5 Flash** and **LaMini-Flan-T5-783M**. It provides instant Q&A, concept explanations, AI-generated quizzes, text summarization, and personalized learning path recommendations — all through a clean, responsive web interface.


Demo Video: `https://drive.google.com/drive/folders/1WcgzrLGywzkeVgJ8YXiANd5XaxnWnwdK`

[Features](#-features) · [Tech Stack](#-tech-stack) · [Quick Start](#-quick-start) · [Project Structure](#-project-structure) · [API Reference](#-api-reference) · [Deployment](#-deployment)

</div>

---

## 📸 Preview

| Q&A Module | Quiz Generator |
|:---:|:---:|
| Ask any educational question and get instant answers | Generate 3 MCQ questions from any topic or passage |

| Explanation Module | Learning Path |
|:---:|:---:|
| Get simple, student-friendly concept explanations | Receive a structured beginner → advanced learning roadmap |

---

## 🎯 Features

| Feature | Description | AI Model |
|---|---|---|
| ❓ **Question Answering** | Get accurate answers to any educational question | Gemini 2.5 Flash |
| 💡 **Concept Explanation** | Simplified explanations for students of all levels | LaMini-Flan-T5-783M |
| 📝 **Text Summarization** | Condense long paragraphs into crisp summaries | Gemini 2.5 Flash |
| 🎯 **Quiz Generation** | Auto-generate 3 MCQ questions with answer checking | Gemini 2.5 Flash |
| 🗺️ **Learning Path** | Personalized study roadmaps (Beginner → Advanced) | Gemini 2.5 Flash |

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | FastAPI + Uvicorn |
| **Frontend** | HTML5 + CSS3 + Vanilla JavaScript (Jinja2 Templates) |
| **AI Model 1** | Google Gemini 2.5 Flash (via `google-generativeai` SDK) |
| **AI Model 2** | MBZUAI/LaMini-Flan-T5-783M (via HuggingFace `transformers`) |
| **Database** | File-based JSON storage |
| **Environment** | Python 3.10+, `python-dotenv` |

---

## 📁 Project Structure

```
edugenie/
│
├── main.py                  # FastAPI app — all routes & endpoints
├── config.py                # Centralized config (API key, app settings)
│
├── qna.py                   # Q&A module (Gemini 2.5 Flash)
├── explanation_module.py    # Explanation module (LaMini-Flan-T5)
├── summary_module.py        # Summarization module (Gemini 2.5 Flash)
├── quiz_module.py           # Quiz generation module (Gemini 2.5 Flash)
├── learning_path.py         # Learning path module (Gemini 2.5 Flash)
│
├── templates/
│   └── index.html           # Main frontend (Jinja2 template)
│
├── static/
│   └── style.css            # Responsive CSS styling
│
├── data/                    # JSON storage directory
│
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

---

## ⚡ Quick Start

### Prerequisites

Before you begin, make sure you have:

- ✅ **Python 3.10+** installed → [Download Python](https://www.python.org/downloads/)
- ✅ **Git** installed → [Download Git](https://git-scm.com/)
- ✅ **Google Gemini API Key** → [Get your free key](https://aistudio.google.com/app/apikey)
- ✅ **VS Code** (recommended) → [Download VS Code](https://code.visualstudio.com/)

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/EduGenie.git
cd EduGenie
```

---

### Step 2 — Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> 💡 You should see `(venv)` at the start of your terminal prompt.

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

> ⏳ **Note:** The first run will download the LaMini-Flan-T5-783M model (~1.5 GB) from HuggingFace. This is a one-time download; it gets cached locally automatically.

---

### Step 4 — Configure Your API Key

1. Copy the environment template:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

2. Open `.env` in your editor and add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

> 🔑 Get your free API key at: **https://aistudio.google.com/app/apikey**

---

### Step 5 — Run the Application

```bash
uvicorn main:app --reload
```

Expected terminal output:
```
INFO:     Will watch for changes in these directories: ['/path/to/edugenie']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process using StatReload
INFO:     Application startup complete.
```

---

### Step 6 — Open in Browser

Navigate to: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

🎉 **EduGenie is now running!**

---

## 🔌 API Reference

All endpoints are also accessible via **Swagger UI** at: `http://127.0.0.1:8000/docs`

### GET `/qa`
Answers an educational question using Gemini 2.5 Flash.

```http
GET /qa?question=Which is the largest ocean?
```
**Response:**
```json
{
  "answer": "The Pacific Ocean is the largest ocean on Earth."
}
```

---

### POST `/explain/`
Explains a concept in simple language using LaMini-Flan-T5.

```http
POST /explain/
Content-Type: application/json

{
  "topic": "Quantum Computing"
}
```
**Response:**
```json
{
  "topic": "Quantum Computing",
  "explanation": "Quantum computing is a type of computing that uses the principles of quantum mechanics..."
}
```

---

### POST `/summarize/`
Summarizes long text using Gemini 2.5 Flash.

```http
POST /summarize/
Content-Type: application/json

{
  "text": "The Industrial Revolution, which began in the late 18th century..."
}
```
**Response:**
```json
{
  "summary": "The Industrial Revolution shifted the world from farming to factories..."
}
```

---

### POST `/quiz`
Generates 3 MCQ questions from a topic or passage using Gemini 2.5 Flash.

```http
POST /quiz
Content-Type: application/json

{
  "text": "Pythagoras theorem"
}
```
**Response:**
```json
{
  "quiz": [
    {
      "question": "What does the Pythagorean theorem describe?",
      "options": ["The relationship between the angles", "The relationship between the sides of a right-angled triangle", "..."],
      "answer": "The relationship between the sides of a right-angled triangle"
    }
  ]
}
```

---

### GET `/learn/recommendations`
Generates a personalized learning path for a topic using Gemini 2.5 Flash.

```http
GET /learn/recommendations?topic=SQL
```
**Response:**
```json
{
  "topic": "SQL",
  "recommendation": "## SQL Learning Path: From Zero to Hero\n\n**I. Beginner Level**..."
}
```

---

## 🗺️ Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                  USER (Browser)                      │
│              http://127.0.0.1:8000                   │
└────────────────────┬────────────────────────────────┘
                     │ HTTP Requests
                     ▼
┌─────────────────────────────────────────────────────┐
│            FastAPI Backend (main.py)                 │
│  ┌──────────┬──────────┬───────────┬──────────────┐ │
│  │  GET /qa │POST      │POST /quiz │GET /learn/   │ │
│  │          │/explain/ │           │recommendations│ │
│  │          │POST      │           │              │ │
│  │          │/summarize│           │              │ │
│  └────┬─────┴────┬─────┴─────┬─────┴──────┬───────┘ │
│       │          │           │            │          │
└───────┼──────────┼───────────┼────────────┼──────────┘
        ▼          ▼           ▼            ▼
  ┌──────────┐ ┌────────┐ ┌────────┐ ┌──────────────┐
  │ Gemini   │ │LaMini- │ │ Gemini │ │ Gemini       │
  │ 2.5 Flash│ │Flan-T5 │ │2.5 Flash│ │ 2.5 Flash    │
  │  (Q&A)   │ │(Explain│ │ (Quiz, │ │  (Learning   │
  │          │ │       )│ │Summarize│ │    Path)     │
  └──────────┘ └────────┘ └────────┘ └──────────────┘
```

---

## 🧪 Testing

Once the server is running, test each feature:

| Feature | How to Test |
|---|---|
| Q&A | Type: *"Why is the sky blue?"* → Click **Get Answer** |
| Explain | Type: *"Binary Search Algorithm"* → Click **Explain** |
| Summarize | Paste a long paragraph → Click **Summarize** |
| Quiz | Type: *"Pythagoras theorem"* → Click **Generate Quiz** → select options → **Check Answer** |
| Learning Path | Type: *"SQL"* → Click **Get Recommendations** |

**API Documentation (Swagger UI):**
```
http://127.0.0.1:8000/docs
```

**Alternative API Documentation (ReDoc):**
```
http://127.0.0.1:8000/redoc
```

---

## 🚀 Deployment

### Option A — Deploy on Render (Free)

1. Push your project to GitHub (see [GitHub Setup](#github-setup) below)
2. Go to [render.com](https://render.com) → **New** → **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Python Version:** `3.13.x` (recommended)
   - **Build Command:** `python -m pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add **Environment Variable:** `GEMINI_API_KEY = your_key_here`
6. Click **Deploy** ✅

### Optional: Automatic Deploys from GitHub → Render

You can trigger Render deploys automatically from GitHub using a workflow that calls the Render API.

1. In your GitHub repo, go to **Settings** → **Secrets and variables** → **Actions** and add two secrets:
  - `RENDER_API_KEY` — your Render account API key (create at https://dashboard.render.com/account/api-keys)
  - `RENDER_SERVICE_ID` — the Render Web Service ID (from your service URL or dashboard)

2. Push to `main` and the workflow `.github/workflows/deploy-to-render.yml` will call the Render API to start a deploy.

3. Monitor deploys in the Render dashboard or check the Actions tab in GitHub for the workflow run.


> If you must use Python `3.14`, use this build command instead:
>
> ```bash
> mkdir -p /tmp/cargo /tmp/rustup && \
> export CARGO_HOME=/tmp/cargo && \
> export RUSTUP_HOME=/tmp/rustup && \
> curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
> . /tmp/cargo/env && \
> python -m pip install -r requirements.txt
> ```
>
> This ensures Rust and Cargo are installed into writable temporary directories so `tokenizers` can build if a wheel is not available.

### Option B — Deploy on Railway

1. Go to [railway.app](https://railway.app)
2. **New Project** → **Deploy from GitHub**
3. Add environment variable: `GEMINI_API_KEY`
4. Railway auto-detects FastAPI and deploys ✅

### Option C — Deploy on Hugging Face Spaces

1. Create a new Space → select **Docker** or **Gradio** template
2. Upload all project files
3. Add Secret: `GEMINI_API_KEY`
4. Space auto-builds and deploys ✅

---

## 📤 GitHub Setup

```bash
# Initialize repository
git init

# Add all files
git add .

# Commit
git commit -m "🎉 Initial commit: EduGenie Learning Assistant"

# Create remote repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/EduGenie.git
git branch -M main
git push -u origin main
```

> ⚠️ **Never push your `.env` file!** It's already in `.gitignore`.

---

## ⚙️ Hardware Requirements

| Component | Minimum | Recommended |
|---|---|---|
| **Processor** | Intel i3 / AMD equivalent | Intel i5 or Apple M1+ |
| **RAM** | 4 GB | 8 GB+ |
| **Storage** | 10 GB free | 15 GB free (for model cache) |
| **Internet** | Required (for Gemini API) | Stable broadband |

---

## 🐛 Troubleshooting

### ❌ `GEMINI_API_KEY is not set!`
→ Make sure `.env` file exists in the project root with your key:
```env
GEMINI_API_KEY=your_actual_key_here
```

### ❌ `ModuleNotFoundError`
→ Ensure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### ❌ `Port 8000 already in use`
→ Use a different port:
```bash
uvicorn main:app --reload --port 8001
```

### ❌ Explanation module takes long to load
→ Normal on first run! LaMini-Flan-T5 (~1.5 GB) is being downloaded and cached. Subsequent runs are instant.

### ❌ `torch` installation fails on Windows
→ Try installing PyTorch separately from [pytorch.org](https://pytorch.org/get-started/locally/)

---

## 📊 ER Diagram – Database Schema

```
USER (1) ──────── (1) USER_QUERY (1) ──────── (1) AI_RESPONSE
                        │
              ┌─────────┼─────────┐
              │         │         │
            (m)        (m)       (m)
        LEARNING_PATH  QUIZ   SUMMARY
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [Google AI Studio](https://aistudio.google.com/) — Gemini 2.5 Flash API
- [MBZUAI](https://huggingface.co/MBZUAI/LaMini-Flan-T5-783M) — LaMini-Flan-T5 model
- [FastAPI](https://fastapi.tiangolo.com/) — High-performance Python web framework
- [HuggingFace Transformers](https://huggingface.co/docs/transformers) — ML model library

---

<div align="center">

**Built with ❤️ using FastAPI + Google Gemini 2.5 Flash**

⭐ Star this repository if you found it helpful!

</div>
