from enum import Enum


class SpotType(Enum):
    REGULAR = "REGULAR"
    HANDICAPPED = "HANDICAPPED"
    EV = "EV"


class SpotStatus(Enum):
    AVAILABLE = "AVAILABLE"
    OCCUPIED = "OCCUPIED"
    OUT_OF_SERVICE = "OUT_OF_SERVICE"


class ParkingSpot:
    def __init__(
        self,
        spot_id,
        lot_id,
        spot_type,
        hourly_rate,
        kwh_rate=0,
        status=SpotStatus.AVAILABLE.value
    ):
        self.spot_id = spot_id
        self.lot_id = lot_id
        self.spot_type = spot_type
        self.status = status
        self.hourly_rate = hourly_rate
        self.kwh_rate = kwh_rate

    def to_dict(self):
        return {
            "spot_id": self.spot_id,
            "lot_id": self.lot_id,
            "spot_type": self.spot_type,
            "status": self.status,
            "hourly_rate": self.hourly_rate,
            "kwh_rate": self.kwh_rate
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            spot_id=data["spot_id"],
            lot_id=data["lot_id"],
            spot_type=data["spot_type"],
            hourly_rate=data["hourly_rate"],
            kwh_rate=data.get("kwh_rate", 0),
            status=data.get("status", SpotStatus.AVAILABLE.value)
        )