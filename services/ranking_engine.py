from rapidfuzz import fuzz


class RankingEngine:

    def score(self, parsed_address, candidate):

        score = 0
        evidence = []

        display = candidate["name"].lower()

        # Landmark
        landmark = parsed_address.landmark
        if landmark:
            s = fuzz.partial_ratio(landmark.lower(), display)
            if s >= 80:
                score += 40
                evidence.append(f"Landmark matched ({s}%)")

        # Locality
        locality = parsed_address.locality
        if locality:
            s = fuzz.partial_ratio(locality.lower(), display)
            if s >= 80:
                score += 25
                evidence.append(f"Locality matched ({s}%)")

        # City
        city = parsed_address.city
        if city:
            s = fuzz.partial_ratio(city.lower(), display)
            if s >= 80:
                score += 15
                evidence.append(f"City matched ({s}%)")

        return {
            "score": score,
            "evidence": evidence
        }