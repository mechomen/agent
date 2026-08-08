from services.address_parser import AddressParser

parser = AddressParser()

address = """
Opp Ganesh Temple,
Sai Nagar,
Vijayawada
"""

result = parser.parse(address)

print(result.model_dump_json(indent=4))