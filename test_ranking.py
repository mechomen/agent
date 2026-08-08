from services.address_parser import AddressParser
from services.osm_service import OSMService
from services.ranking_engine import RankingEngine

parser = AddressParser()
osm = OSMService()
ranker = RankingEngine()

address = """
Opp Ganesh Temple,
Sai Nagar,
Vijayawada
"""

parsed = parser.parse(address)

results = osm.search(
    f"{parsed.landmark} {parsed.city}"
)

for candidate in results:

    ranking = ranker.score(parsed, candidate)

    print("-" * 60)

    print(candidate["name"])

    print("Score:", ranking["score"])

    print("Evidence:", ranking["evidence"])