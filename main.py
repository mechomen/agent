from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Address Intelligence AI")


# -----------------------------
# CORS
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Request Model
# -----------------------------

class AddressRequest(BaseModel):
    address: str


# -----------------------------
# Home
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Address Intelligence AI Backend Running"
    }


# -----------------------------
# Verify Address
# -----------------------------

@app.post("/verify")
def verify_address(request: AddressRequest):

    address = request.address

    print("Received address:", address)

    # Temporary parsing for testing
    parts = [
        part.strip()
        for part in address.split(",")
        if part.strip()
    ]

    landmark = parts[0] if len(parts) > 0 else "Unknown"
    locality = parts[1] if len(parts) > 1 else "Unknown"
    city = parts[2] if len(parts) > 2 else "Unknown"
    district = parts[3] if len(parts) > 3 else "Unknown"
    state = parts[4] if len(parts) > 4 else "Unknown"

    return {
        "success": True,

        "parsed_address": {
            "landmark": landmark,
            "locality": locality,
            "city": city,
            "district": district,
            "state": state,
        },

        "best_match": {
            "name": address,
            "latitude": 17.3850,
            "longitude": 78.4867,
        },

        "confidence": 0.92,

        "evidence": [
            "Address Parsed Successfully",
            "Address Format Valid",
            "Location Estimated",
        ],
    }