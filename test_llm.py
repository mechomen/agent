from services.llm_service import LLMService

llm = LLMService()

response = llm.ask("Reply with only one word: SUCCESS")

print(response)