"""
EduGenie - Summary Module
Uses Google Gemini 1.5 Pro to summarize long educational text.
"""

import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)


def summarize_text(text: str) -> str:
    """
    Summarizes a given piece of educational text using Gemini.

    Args:
        text: The long text or paragraph to summarize.

    Returns:
        A string containing the concise summary.
    """
    try:
        model = genai.GenerativeModel(model_name=GEMINI_MODEL_NAME)
        prompt = f"Summarize the following text in simple language:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in Summary: {e}"
