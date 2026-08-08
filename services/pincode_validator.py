import csv


class PincodeValidator:

    def __init__(self):

        self.records = []

        with open(
            "data/pincode.csv",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            self.records = list(reader)

    def search(self, keyword):

        keyword = keyword.lower().strip()

        matches = []

        for row in self.records:

            office = row["officename"].lower()
            district = row["district"].lower()
            state = row["statename"].lower()
            pin = row["pincode"]

            if (
                keyword in office
                or keyword in district
                or keyword in state
                or keyword == pin
            ):

                matches.append({
                    "office": row["officename"],
                    "district": row["district"],
                    "state": row["statename"],
                    "pincode": row["pincode"],
                    "latitude": row["latitude"],
                    "longitude": row["longitude"]
                })

        return matches