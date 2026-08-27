import json
import os
from datetime import datetime

from models.parking_lot import ParkingLot
from models.parking_spot import ParkingSpot
from models.vehicle import Vehicle
from models.parking_session import ParkingSession
from models.charging_session import ChargingSession

from exceptions import *


class FacilityManager:

    def __init__(self):
        self.data_dir = "data"

        self.lots_file = os.path.join(
            self.data_dir,
            "lots.json"
        )

        self.spots_file = os.path.join(
            self.data_dir,
            "spots.json"
        )

        self.vehicles_file = os.path.join(
            self.data_dir,
            "vehicles.json"
        )

        self.parking_sessions_file = os.path.join(
            self.data_dir,
            "parking_sessions.json"
        )

        self.charging_sessions_file = os.path.join(
            self.data_dir,
            "charging_sessions.json"
        )

        self._load_all_data()


    # ==================================
    # JSON METHODS
    # ==================================

    def _load_json(self, file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []


    def _save_json(self, file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)


    def _load_all_data(self):
        self.lots = self._load_json(
            self.lots_file
        )

        self.spots = self._load_json(
            self.spots_file
        )

        self.vehicles = self._load_json(
            self.vehicles_file
        )

        self.parking_sessions = self._load_json(
            self.parking_sessions_file
        )

        self.charging_sessions = self._load_json(
            self.charging_sessions_file
        )


    # ==================================
    # PARKING LOT METHODS
    # ==================================

    def add_lot(self, lot_id, name, location):

        for item in self.lots:
            if item["lot_id"] == lot_id:
                raise DuplicateLotError(
                    f"Parking lot '{lot_id}' already exists."
                )

        lot = ParkingLot(
            lot_id=lot_id,
            name=name,
            location=location
        )

        self.lots.append(
            lot.to_dict()
        )

        self._save_json(
            self.lots_file,
            self.lots
        )

        return lot


    def get_lot(self, lot_id):

        for item in self.lots:
            if item["lot_id"] == lot_id:
                return ParkingLot.from_dict(
                    item
                )

        raise ValueError(
            f"Parking lot '{lot_id}' not found."
        )


    def get_all_lots(self):

        return [
            ParkingLot.from_dict(item)
            for item in self.lots
        ]


    # ==================================
    # PARKING SPOT METHODS
    # ==================================

    def add_spot(
        self,
        spot_id,
        lot_id,
        spot_type,
        hourly_rate,
        kwh_rate=0
    ):

        self.get_lot(lot_id)

        for item in self.spots:
            if item["spot_id"] == spot_id:
                raise DuplicateSpotError(
                    f"Parking spot '{spot_id}' already exists."
                )

        if hourly_rate <= 0:
            raise InvalidRateError(
                "Hourly rate must be greater than zero."
            )

        if spot_type == "EV" and kwh_rate <= 0:
            raise InvalidRateError(
                "kWh rate must be greater than zero for EV spots."
            )

        if spot_type != "EV":
            kwh_rate = 0

        spot = ParkingSpot(
            spot_id=spot_id,
            lot_id=lot_id,
            spot_type=spot_type,
            hourly_rate=hourly_rate,
            kwh_rate=kwh_rate
        )

        self.spots.append(
            spot.to_dict()
        )

        for lot in self.lots:
            if lot["lot_id"] == lot_id:
                lot["spot_ids"].append(
                    spot_id
                )
                break

        self._save_json(
            self.spots_file,
            self.spots
        )

        self._save_json(
            self.lots_file,
            self.lots
        )

        return spot


    def get_spot(self, spot_id):

        for item in self.spots:
            if item["spot_id"] == spot_id:
                return ParkingSpot.from_dict(
                    item
                )

        raise ValueError(
            f"Parking spot '{spot_id}' not found."
        )


    def get_all_spots(self):

        return [
            ParkingSpot.from_dict(item)
            for item in self.spots
        ]


    def update_spot(self, spot_id, **updates):

        self.get_spot(spot_id)

        for item in self.spots:

            if item["spot_id"] == spot_id:

                if "hourly_rate" in updates:
                    if updates["hourly_rate"] <= 0:
                        raise InvalidRateError(
                            "Hourly rate must be greater than zero."
                        )

                if "kwh_rate" in updates:
                    if updates["kwh_rate"] < 0:
                        raise InvalidRateError(
                            "kWh rate cannot be negative."
                        )

                item.update(
                    updates
                )

                break

        self._save_json(
            self.spots_file,
            self.spots
        )

        return self.get_spot(
            spot_id
        )


    def delete_spot(self, spot_id):

        spot = self.get_spot(
            spot_id
        )

        if spot.status == "OCCUPIED":
            raise SpotOccupiedError(
                "Cannot delete an occupied parking spot."
            )

        self.spots = [
            item
            for item in self.spots
            if item["spot_id"] != spot_id
        ]

        for lot in self.lots:
            if spot_id in lot["spot_ids"]:
                lot["spot_ids"].remove(
                    spot_id
                )
                break

        self._save_json(
            self.spots_file,
            self.spots
        )

        self._save_json(
            self.lots_file,
            self.lots
        )

        return True


    # ==================================
    # VEHICLE METHODS
    # ==================================

    def register_vehicle(
        self,
        license_plate,
        owner_name,
        vehicle_type
    ):

        for item in self.vehicles:
            if item["plate"] == license_plate:
                raise DuplicateVehicleError(
                    f"Vehicle '{license_plate}' already exists."
                )

        vehicle = Vehicle(
            plate=license_plate,
            owner_name=owner_name,
            vehicle_type=vehicle_type
        )

        self.vehicles.append(
            vehicle.to_dict()
        )

        self._save_json(
            self.vehicles_file,
            self.vehicles
        )

        return vehicle


    def get_vehicle(self, license_plate):

        for item in self.vehicles:
            if item["plate"] == license_plate:
                return Vehicle.from_dict(
                    item
                )

        raise ValueError(
            f"Vehicle '{license_plate}' not found."
        )


    def get_all_vehicles(self):

        return [
            Vehicle.from_dict(item)
            for item in self.vehicles
        ]
    # ==================================
    # PARKING SESSION METHODS
    # ==================================

    def start_parking(self, license_plate, spot_id):

        # Check that vehicle is registered
        vehicle = self.get_vehicle(license_plate)

        # Check that parking spot exists
        spot = self.get_spot(spot_id)

        # Check that the spot is available
        if spot.status != "AVAILABLE":
            raise SpotOccupiedError(
                f"Parking spot '{spot_id}' is not available."
            )

        # Check if vehicle is already parked
        for item in self.parking_sessions:
            if (
                item["plate"] == license_plate
                and item["status"] == "ACTIVE"
            ):
                raise ValueError(
                    f"Vehicle '{license_plate}' is already parked."
                )

        # Create parking session
        session = ParkingSession(
            plate=vehicle.plate,
            spot_id=spot.spot_id,
            lot_id=spot.lot_id
        )

        self.parking_sessions.append(
            session.to_dict()
        )

        # Change spot status to OCCUPIED
        for item in self.spots:
            if item["spot_id"] == spot_id:
                item["status"] = "OCCUPIED"
                break

        # Save changes
        self._save_json(
            self.parking_sessions_file,
            self.parking_sessions
        )

        self._save_json(
            self.spots_file,
            self.spots
        )

        return session


    def end_parking(self, license_plate):

        # Find active parking session
        active_session = None

        for item in self.parking_sessions:
            if (
                item["plate"] == license_plate
                and item["status"] == "ACTIVE"
            ):
                active_session = item
                break

        if active_session is None:
            raise ValueError(
                f"No active parking session found "
                f"for vehicle '{license_plate}'."
            )

        # Get parking spot
        spot = self.get_spot(
            active_session["spot_id"]
        )

        # Create ParkingSession object
        session = ParkingSession.from_dict(
            active_session
        )

        # Set check-out time
        session.check_out_time = (
            __import__("datetime").datetime.now().isoformat()
        )

        # Calculate parking fee
        session.calculate_fee(
            spot.hourly_rate
        )

        # Mark session as completed
        session.status = "COMPLETED"

        # Update session data
        for index, item in enumerate(
            self.parking_sessions
        ):
            if (
                item["session_id"]
                == session.session_id
            ):
                self.parking_sessions[index] = (
                    session.to_dict()
                )
                break

        # Make parking spot available again
        for item in self.spots:
            if (
                item["spot_id"]
                == session.spot_id
            ):
                item["status"] = "AVAILABLE"
                break

        # Save changes
        self._save_json(
            self.parking_sessions_file,
            self.parking_sessions
        )

        self._save_json(
            self.spots_file,
            self.spots
        )

        return session


    def get_active_parking_sessions(self):

        return [
            ParkingSession.from_dict(item)
            for item in self.parking_sessions
            if item["status"] == "ACTIVE"
        ]
           # ==================================
    # CHARGING SESSION METHODS
    # ==================================

    def start_charging(self, license_plate, spot_id):

        vehicle = self.get_vehicle(
            license_plate
        )

        if vehicle.vehicle_type != "EV_CAR":
            raise ValueError(
                "Only EV vehicles can use charging."
            )

        spot = self.get_spot(
            spot_id
        )

        if spot.spot_type != "EV":
            raise ValueError(
                "Charging is only available at EV spots."
            )

        if spot.status != "AVAILABLE":
            raise SpotOccupiedError(
                f"Parking spot '{spot_id}' is not available."
            )

        for item in self.charging_sessions:

            if (
                item["plate"] == license_plate
                and item["status"] == "ACTIVE"
            ):
                raise ValueError(
                    f"Vehicle '{license_plate}' "
                    "already has an active charging session."
                )

        session = ChargingSession(
            plate=license_plate,
            spot_id=spot_id
        )

        self.charging_sessions.append(
            session.to_dict()
        )

        for item in self.spots:

            if item["spot_id"] == spot_id:
                item["status"] = "OCCUPIED"
                break

        self._save_json(
            self.charging_sessions_file,
            self.charging_sessions
        )

        self._save_json(
            self.spots_file,
            self.spots
        )

        return session


    def end_charging(
        self,
        license_plate,
        energy_used
    ):

        active_session = None

        for item in self.charging_sessions:

            if (
                item["plate"] == license_plate
                and item["status"] == "ACTIVE"
            ):
                active_session = item
                break

        if active_session is None:
            raise ValueError(
                f"No active charging session found "
                f"for '{license_plate}'."
            )

        if energy_used < 0:
            raise ValueError(
                "Energy used cannot be negative."
            )

        spot = self.get_spot(
            active_session["spot_id"]
        )

        session = ChargingSession.from_dict(
            active_session
        )

        session.end_time = (
            datetime.now().isoformat()
        )

        session.energy_used = energy_used

        session.calculate_fee(
            spot.kwh_rate
        )

        session.status = "COMPLETED"

        for index, item in enumerate(
            self.charging_sessions
        ):

            if (
                item["session_id"]
                == session.session_id
            ):
                self.charging_sessions[index] = (
                    session.to_dict()
                )
                break

        for item in self.spots:

            if (
                item["spot_id"]
                == session.spot_id
            ):
                item["status"] = "AVAILABLE"
                break

        self._save_json(
            self.charging_sessions_file,
            self.charging_sessions
        )

        self._save_json(
            self.spots_file,
            self.spots
        )

        return session


    def get_active_charging_sessions(self):

        return [
            ChargingSession.from_dict(item)
            for item in self.charging_sessions
            if item["status"] == "ACTIVE"
        ]