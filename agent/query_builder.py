class QueryBuilder:
    
    def build(self, parsed):

        queries = []

        if parsed.landmark and parsed.city:
            queries.append(f"{parsed.landmark} {parsed.city}")

        if parsed.locality and parsed.city:
            queries.append(f"{parsed.locality} {parsed.city}")

        if parsed.landmark and parsed.locality:
            queries.append(f"{parsed.landmark} {parsed.locality}")

        if parsed.city:
            queries.append(parsed.city)

        if parsed.landmark:
            queries.append(parsed.landmark)

        # Remove duplicates
        unique = []
        seen = set()

        for q in queries:
            q = q.strip()

            if q.lower() not in seen:
                seen.add(q.lower())
                unique.append(q)

        return unique