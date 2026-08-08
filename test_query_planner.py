from services.address_parser import AddressParser
from agent.query_planner import QueryPlanner

parser = AddressParser()
planner = QueryPlanner()

address = """
Opp Ganesh Temple,
Sai Nagar,
Vijayawada
"""

parsed = parser.parse(address)

queries = planner.generate_queries(parsed)

print("\nGenerated Queries\n")

for i, q in enumerate(queries, start=1):

    print(f"{i}. {q}")