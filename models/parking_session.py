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
        Calculate parking fee based on parking duration.
        Minimum charge is for 1 hour.
        """

        if not self.check_out_time:
            self.check_out_time = datetime.now().isoformat()

        check_in = datetime.fromisoformat(self.check_in_time)
        check_out = datetime.fromisoformat(self.check_out_time)

        duration_seconds = (
            check_out - check_in
        ).total_seconds()

        duration_hours = duration_seconds / 3600

        # Minimum charge: 1 hour
        charged_hours = max(1, duration_hours)

        self.parking_fee = round(
            charged_hours * hourly_rate,
            2
        )

        return self.parking_fee

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