import uuid
from datetime import datetime


class ChargingSession:

    def __init__(
        self,
        plate,
        spot_id,
        session_id=None,
        start_time=None,
        end_time=None,
        energy_used=0,
        charging_fee=0,
        status="ACTIVE"
    ):
        self.session_id = session_id or str(uuid.uuid4())
        self.plate = plate
        self.spot_id = spot_id

        self.start_time = (
            start_time or datetime.now().isoformat()
        )

        self.end_time = end_time
        self.energy_used = energy_used
        self.charging_fee = charging_fee
        self.status = status

    def calculate_fee(self, kwh_rate):
        """
        Calculate EV charging fee
        based on energy used in kWh.
        """

        self.charging_fee = round(
            self.energy_used * kwh_rate,
            2
        )

        return self.charging_fee

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "plate": self.plate,
            "spot_id": self.spot_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "energy_used": self.energy_used,
            "charging_fee": self.charging_fee,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            plate=data["plate"],
            spot_id=data["spot_id"],
            session_id=data["session_id"],
            start_time=data["start_time"],
            end_time=data.get("end_time"),
            energy_used=data.get("energy_used", 0),
            charging_fee=data.get("charging_fee", 0),
            status=data.get("status", "ACTIVE")
        )