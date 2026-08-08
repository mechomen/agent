from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME


class LLMService:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def ask(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content