"""
EduGenie Learning Assistant – Main Application
FastAPI backend with endpoints for all AI-powered educational features.

Endpoints:
  GET  /              → Renders the main HTML interface
  GET  /qa            → Q&A using Google Gemini
  POST /explain/      → Concept explanation using LaMini-Flan-T5
  POST /summarize/    → Text summarization using Google Gemini
  POST /quiz          → MCQ Quiz generation using Google Gemini
  GET  /learn/recommendations → Learning path using Google Gemini

Run with:
  uvicorn main:app --reload
"""

from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import APP_TITLE, APP_VERSION, APP_DESCRIPTION
from qna import answer_question_with_gemini
from explanation_module import explain_topic
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations

# ── App Initialization ────────────────────────────────────────────────────
app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description=APP_DESCRIPTION
)

# ── Static Files & Templates ──────────────────────────────────────────────
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# ── Root – Serve HTML Interface ───────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Renders the main EduGenie frontend interface."""
    return templates.TemplateResponse("index.html", {"request": request})


# ── Q&A – GET API using Gemini ────────────────────────────────────────────
@app.get("/qa")
async def answer_question(question: str = Query(..., description="Educational question to answer")):
    """
    Answers an educational question using Google Gemini 2.5 Flash.

    Example: GET /qa?question=What is photosynthesis?
    """
    answer = answer_question_with_gemini(question)
    return {"answer": answer}


# ── Explanation – POST API using LaMini-Flan-T5 ───────────────────────────
@app.post("/explain/")
async def explain_api(request: Request):
    """
    Explains a concept in simple language using LaMini-Flan-T5.

    Body: {"topic": "Photosynthesis"}
    """
    data = await request.json()
    topic = data.get("topic")

    if not topic:
        return JSONResponse(
            content={"error": "Please provide a topic."},
            status_code=400
        )

    explanation = explain_topic(topic)
    return {"topic": topic, "explanation": explanation}


# ── Summarization – POST API using Gemini ─────────────────────────────────
@app.post("/summarize/")
async def summarize_api(request: Request):
    """
    Summarizes long educational text using Gemini 2.5 Flash.

    Body: {"text": "Long passage here..."}
    """
    data = await request.json()
    text = data.get("text")

    if not text:
        return JSONResponse(
            content={"error": "Please provide text to summarize."},
            status_code=400
        )

    summary = summarize_text(text)
    return {"summary": summary}


# ── Quiz Generation – POST API using Gemini ───────────────────────────────
@app.post("/quiz")
async def quiz_api(request: Request):
    """
    Generates 3 MCQ questions from a topic or passage using Gemini 2.5 Flash.

    Body: {"text": "Pythagoras theorem"}
    """
    data = await request.json()
    text = data.get("text")

    if not text:
        return JSONResponse(
            content={"error": "Please provide text for quiz."},
            status_code=400
        )

    quiz = generate_quiz(text)
    print("Generated quiz:", quiz)  # ✅ DEBUG: visible in terminal
    return JSONResponse(content={"quiz": quiz})


# ── Learning Recommendations – GET API using Gemini ───────────────────────
@app.get("/learn/recommendations")
async def learning_recommendation_api(
    topic: str = Query(..., description="Topic to get learning recommendations for")
):
    """
    Generates a structured, personalized learning path for a topic.

    Example: GET /learn/recommendations?topic=Machine Learning
    """
    recommendation = get_learning_recommendations(topic)
    return {"topic": topic, "recommendation": recommendation}
