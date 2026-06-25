"""
EduGenie - Learning Path Module
Uses Google Gemini 2.5 Flash to generate personalized, structured learning paths.
Covers beginner → intermediate → advanced levels with resources.
"""

import traceback
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model once at module level
model = genai.GenerativeModel(model_name=GEMINI_MODEL_NAME)


def get_learning_recommendations(topic: str) -> str:
    """
    Generates a personalized, structured learning path for a given topic.

    Args:
        topic: The subject or topic the student wants to learn.

    Returns:
        A detailed learning path string from beginner to advanced level,
        including resources and study recommendations.
    """
    prompt = f"""You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured and adaptive learning path including key topics, order of learning, and resources (videos, books, online courses).
Include beginner, intermediate, and advanced levels if needed.
"""

    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return response.text
        elif hasattr(response, "parts") and response.parts:
            return response.parts[0].text
        else:
            return "❌ Could not extract content from Gemini response."

    except Exception as e:
        traceback.print_exc()  # ✅ Prints full error trace in terminal
        return f"❌ Error occurred: {str(e)}"
