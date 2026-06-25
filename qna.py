"""
EduGenie - Q&A Module
Uses Google Gemini 1.5 Pro to answer educational questions.
"""

import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)


def answer_question_with_gemini(question: str) -> str:
    """
    Answers an educational question using Google Gemini.

    Args:
        question: The question string from the user.

    Returns:
        A string containing the AI-generated answer.
    """
    try:
        model = genai.GenerativeModel(model_name=GEMINI_MODEL_NAME)
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in QnA: {e}"
