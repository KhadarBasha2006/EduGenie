"""
EduGenie - Configuration Module
Centralized configuration for API keys and application settings.

⚠️  IMPORTANT: Never commit your actual API key to version control.
    Set GEMINI_API_KEY as an environment variable or use a .env file.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

# ── Google Gemini API Key ──────────────────────────────────────────────────
# Set this in your .env file:  GEMINI_API_KEY=your_key_here
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

if not GEMINI_API_KEY:
    raise ValueError(
        "❌ GEMINI_API_KEY is not set!\n"
        "   Please create a .env file with:  GEMINI_API_KEY=your_actual_key\n"
        "   Get your key at: https://aistudio.google.com/app/apikey"
    )

# ── Default Gemini Model Name ───────────────────────────────────────────────
# Override this in .env if needed: GEMINI_MODEL_NAME=models/gemini-2.5-flash
GEMINI_MODEL_NAME: str = os.getenv("GEMINI_MODEL_NAME", "models/gemini-2.5-flash")

# ── Application Settings ───────────────────────────────────────────────────
APP_TITLE = "EduGenie Learning Assistant"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = (
    "An AI-powered educational assistant for Q&A, explanations, "
    "quiz generation, summarization, and personalized learning paths."
)
