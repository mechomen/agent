from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    house_number: Optional[str] = None
    building_name: Optional[str] = None
    landmark: Optional[str] = None
    street: Optional[str] = None
    locality: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None
    confidence: float