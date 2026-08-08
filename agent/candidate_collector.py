class CandidateCollector:
    
    def __init__(self, osm):
        self.osm = osm
        
    def collect(self, queries):

        all_candidates = []

        for query in queries:

            print(f"\nSearching : {query}")

            results = self.osm.search(query)

            print(f"Found {len(results)} locations")

            all_candidates.extend(results)

        return all_candidates