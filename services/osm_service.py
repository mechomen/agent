import requests


class OSMService:

    def __init__(self):
        self.url = "https://nominatim.openstreetmap.org/search"

    def search(self, query):

        headers = {
            "User-Agent": "AddressIntelligenceAgent/1.0"
        }

        params = {
            "q": query,
            "format": "jsonv2",
            "limit": 5
        }

        response = requests.get(
            self.url,
            params=params,
            headers=headers,
            timeout=20
        )

        if response.status_code != 200:
            return []

        data = response.json()

        results = []

        for item in data:

            results.append({
                "name": item.get("display_name"),
                "latitude": item.get("lat"),
                "longitude": item.get("lon"),
                "type": item.get("type")
            })

        return results