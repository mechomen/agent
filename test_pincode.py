from services.pincode_validator import PincodeValidator

validator = PincodeValidator()

results = validator.search("Vijayawada")

print(f"Found {len(results)} matches\n")

for r in results[:5]:
    print(r)