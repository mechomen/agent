import json

from models.address import Address
from prompts.parser_prompt import ADDRESS_PARSER_PROMPT
from services.ai_engine import AIEngine


class AddressParser:

    def __init__(self):
        self.ai = AIEngine()

    def parse(self, raw_address: str):

        prompt = f"""
{ADDRESS_PARSER_PROMPT}

Address:

{raw_address}
"""

        response = self.ai.ask(prompt)

        # Remove Markdown if the model returns ```json ... ```
        response = response.replace("```json", "").replace("```", "").strip()

        data = json.loads(response)

        return Address(**data)