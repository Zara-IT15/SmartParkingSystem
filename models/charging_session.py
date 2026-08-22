import uuid
from datetime import datetime


class ChargingSession:
    def __init__(
        self,
        parking_session_id,
        start_meter,
        charging_session_id=None,
        start_time=None,
        end_time=None,
        end_meter=None,
        energy_cost=0,
        status="ACTIVE"
    ):
        self.charging_session_id = (
            charging_session_id or str(uuid.uuid4())
        )
        self.parking_session_id = parking_session_id
        self.start_time = start_time or datetime.now().isoformat()
        self.end_time = end_time
        self.start_meter = start_meter
        self.end_meter = end_meter
        self.energy_cost = energy_cost
        self.status = status

    def calculate_cost(self, kwh_rate):
        """
        Charging cost calculation will be implemented
        when we build the charging logic.
        """
        return 0

    def to_dict(self):
        return {
            "charging_session_id": self.charging_session_id,
            "parking_session_id": self.parking_session_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "start_meter": self.start_meter,
            "end_meter": self.end_meter,
            "energy_cost": self.energy_cost,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            parking_session_id=data["parking_session_id"],
            start_meter=data["start_meter"],
            charging_session_id=data["charging_session_id"],
            start_time=data["start_time"],
            end_time=data.get("end_time"),
            end_meter=data.get("end_meter"),
            energy_cost=data.get("energy_cost", 0),
            status=data.get("status", "ACTIVE")
        )