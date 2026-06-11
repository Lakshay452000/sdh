from google import genai
from google.genai import types
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
    
    def analyze_image(
            self,
            image_bytes: bytes,
            prompt: str
    ) -> str:

        logger.info("Calling Gemini Vision")

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                prompt,
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png"
                )
            ]
        )

        return response.text