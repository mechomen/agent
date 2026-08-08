from services.ai_engine import AIEngine

ai = AIEngine()

response = ai.ask("Reply with only one word: SUCCESS")

print(response)
