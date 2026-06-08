from prompt import get_review_prompt
import os
import json

from dotenv import load_dotenv
from google import genai

from prompt import get_review_prompt
from langfuse_config import langfuse

load_dotenv()

MODEL_NAME = "gemini-2.5-flash-lite"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def review_code(code_snippet):

    prompt = get_review_prompt(code_snippet)

    try:

        with langfuse.start_as_current_observation(
            name="code-review"
        ):

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            result = response.text.strip()

            # Remove markdown code blocks if Gemini returns them
            result = result.replace("```json", "")
            result = result.replace("```", "")
            result = result.strip()

            try:
                parsed_result = json.loads(result)

            except json.JSONDecodeError:

                parsed_result = {
                    "identified_issues": [],
                    "improvement_suggestions": [],
                    "code_quality_level": "Unknown",
                    "review_summary": result
                }

            langfuse.flush()

            return parsed_result

    except Exception as e:

        langfuse.flush()

        return {
            "identified_issues": [],
            "improvement_suggestions": [],
            "code_quality_level": "Error",
            "review_summary": str(e)
        }