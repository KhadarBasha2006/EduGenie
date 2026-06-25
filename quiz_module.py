"""
EduGenie - Quiz Module
Uses Google Gemini 2.5 Flash to generate multiple-choice questions (MCQs).
Returns structured JSON with questions, options, and correct answers.
"""

import re
import json
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)


def clean_json_block(text: str) -> str:
    """
    Removes Markdown ```json ... ``` code fences from model output.

    Args:
        text: Raw text string potentially containing Markdown code fences.

    Returns:
        Clean JSON string without fences.
    """
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()


def generate_quiz(text: str) -> list:
    """
    Generates 3 multiple-choice questions from a given passage using Gemini.

    Args:
        text: The topic or passage to generate questions from.

    Returns:
        A list of dicts with 'question', 'options' (list of 4), and 'answer'.
        Returns an error dict in a list if something goes wrong.
    """
    try:
        model = genai.GenerativeModel(model_name=GEMINI_MODEL_NAME)

        prompt = f"""You are a quiz generator.

From the following passage, create 3 multiple-choice questions. Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON**, like this:
[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{text}
"""

        response = model.generate_content(prompt)
        quiz_text = response.text.strip()

        # 🧹 Clean Markdown code blocks if present
        cleaned_text = clean_json_block(quiz_text)

        # Parse the JSON
        quiz_data = json.loads(cleaned_text)
        return quiz_data

    except json.JSONDecodeError as je:
        return [{"error": f"JSON parsing failed: {je}", "raw": quiz_text}]
    except Exception as e:
        return [{"error": f"Quiz generation failed: {str(e)}"}]
