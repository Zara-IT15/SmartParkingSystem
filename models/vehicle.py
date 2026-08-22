from datetime import datetime
from enum import Enum


class VehicleType(Enum):
    CAR = "CAR"
    MOTORCYCLE = "MOTORCYCLE"
    EV_CAR = "EV_CAR"


class Vehicle:
    def __init__(
        self,
        plate,
        owner_name,
        vehicle_type,
        registered_date=None
    ):
        self.plate = plate
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type
        self.registered_date = (
            registered_date
            if registered_date
            else datetime.now().isoformat()
        )

    def to_dict(self):
        return {
            "plate": self.plate,
            "owner_name": self.owner_name,
            "vehicle_type": self.vehicle_type,
            "registered_date": self.registered_date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            plate=data["plate"],
            owner_name=data["owner_name"],
            vehicle_type=data["vehicle_type"],
            registered_date=data["registered_date"]
        )