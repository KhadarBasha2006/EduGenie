"""
EduGenie - Explanation Module
Uses Google Gemini to explain topics in simple, clear language.
"""

import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def explain_topic(topic: str) -> str:
    """
    Explains a given topic in a simple and clear way using Gemini.

    Args:
        topic: The educational topic or concept to explain.

    Returns:
        A string containing the simplified explanation.
    """
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
    response = model.generate_content(
        f"Explain the concept of '{topic}' in a simple and clear way for a school student."
    )
    return response.text.strip()
