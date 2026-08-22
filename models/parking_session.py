import uuid
from datetime import datetime


class ParkingSession:
    def __init__(
        self,
        plate,
        spot_id,
        lot_id,
        session_id=None,
        check_in_time=None,
        check_out_time=None,
        parking_fee=0,
        status="ACTIVE"
    ):
        self.session_id = session_id or str(uuid.uuid4())
        self.plate = plate
        self.spot_id = spot_id
        self.lot_id = lot_id
        self.check_in_time = check_in_time or datetime.now().isoformat()
        self.check_out_time = check_out_time
        self.parking_fee = parking_fee
        self.status = status

    def calculate_fee(self, hourly_rate):
        """
        Parking fee calculation will be implemented
        when we build the billing logic.
        """
        return 0

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "plate": self.plate,
            "spot_id": self.spot_id,
            "lot_id": self.lot_id,
            "check_in_time": self.check_in_time,
            "check_out_time": self.check_out_time,
            "parking_fee": self.parking_fee,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            plate=data["plate"],
            spot_id=data["spot_id"],
            lot_id=data["lot_id"],
            session_id=data["session_id"],
            check_in_time=data["check_in_time"],
            check_out_time=data.get("check_out_time"),
            parking_fee=data.get("parking_fee", 0),
            status=data.get("status", "ACTIVE")
        )