from agent.orchestrator import AddressAgent

agent = AddressAgent()

address = """
Opp Ganesh Temple,
Sai Nagar,
Vijayawada
"""

result = agent.process(address)

print("\n")
print("=" * 60)
print("FINAL RESULT")
print("=" * 60)

for key, value in result.items():
    print(f"{key} : {value}")