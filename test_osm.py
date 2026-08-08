from services.osm_service import OSMService

osm = OSMService()

results = osm.search("Ganesh Temple Vijayawada")

print(f"\nFound {len(results)} Results\n")

for r in results:
    print(r)