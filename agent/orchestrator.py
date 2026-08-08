from services.address_parser import AddressParser
from services.pincode_validator import PincodeValidator
from services.ranking_engine import RankingEngine

from services.osm_service import OSMService
from agent.query_builder import QueryBuilder
from agent.candidate_collector import CandidateCollector
from agent.duplicate_remover import DuplicateRemover


class AddressAgent:

    def __init__(self):

        self.parser = AddressParser()

        self.validator = PincodeValidator()

        self.osm = OSMService()

        self.ranker = RankingEngine()

        self.planner = QueryBuilder()

        self.collector = CandidateCollector(self.osm)
        self.builder = QueryBuilder()
        self.remover = DuplicateRemover()

    def process(self, address: str):

        print("\n====================================")
        print("STEP 1 : ADDRESS PARSING")
        print("====================================")

        parsed = self.parser.parse(address)

        print(parsed)

        print("\n====================================")
        print("STEP 2 : PINCODE DATASET SEARCH")
        print("====================================")

        dataset_results = []

        if parsed.city:
            dataset_results = self.validator.search(parsed.city)

        print(f"Dataset Matches : {len(dataset_results)}")

        print("\n====================================")
        print("STEP 3 : AI QUERY BUILDER")
        print("====================================")

        queries = self.builder.build(parsed)

        for i, q in enumerate(queries, start=1):
            print(f"{i}. {q}")

        print("\n====================================")
        print("STEP 4 : OSM CANDIDATE COLLECTION")
        print("====================================")

        candidates = self.collector.collect(queries)

        print(f"\nCollected {len(candidates)} Candidates")

        print("\n====================================")
        print("STEP 5 : REMOVE DUPLICATES")
        print("====================================")

        candidates = self.remover.remove(candidates)

        print(f"Unique Candidates : {len(candidates)}")

        print("\n====================================")
        print("STEP 6 : RANKING")
        print("====================================")

        ranked = []

        for candidate in candidates:

            result = self.ranker.score(parsed, candidate)

            ranked.append({

                "candidate": candidate,

                "score": result["score"],

                "evidence": result["evidence"]

            })

        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        print()

        for i, item in enumerate(ranked, start=1):

            print("--------------------------------------------")

            print(f"Rank #{i}")

            print(item["candidate"]["name"])

            print("Score :", item["score"])

            print("Evidence :")

            for e in item["evidence"]:
                print("  ✓", e)

            print()

        print("====================================")
        print("STEP 7 : BEST MATCH")
        print("====================================")

        if len(ranked) == 0:

            return {
                "success": False,
                "message": "No matching location found."
            }

        best = ranked[0]

        return {

            "success": True,

            "parsed_address": parsed.model_dump(),

            "dataset_matches": len(dataset_results),

            "total_candidates": len(candidates),

            "best_match": best["candidate"],

            "score": best["score"],

            "confidence": round(best["score"] / 100, 2),

            "evidence": best["evidence"]

        }