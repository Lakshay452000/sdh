from google import genai

from app.core.logger import logger
from app.config.settings import settings


class GeminiService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def ask(self, prompt: str) -> str:
        logger.info("Calling Gemini")

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text