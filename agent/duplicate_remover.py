class DuplicateRemover:
    
    def remove(self, candidates):

        unique = []

        seen = set()

        for candidate in candidates:

            key = (
                candidate["name"].lower(),
                candidate["latitude"],
                candidate["longitude"]
            )

            if key not in seen:

                seen.add(key)

                unique.append(candidate)

        return unique