class ParkingError(Exception):
    """Base exception for the Smart Parking System."""
    pass


class DuplicateLotError(ParkingError):
    pass


class DuplicateSpotError(ParkingError):
    pass


class DuplicateVehicleError(ParkingError):
    pass


class VehicleAlreadyCheckedInError(ParkingError):
    pass


class IncompatibleSpotError(ParkingError):
    pass


class NoCompatibleSpotError(ParkingError):
    pass


class SessionAlreadyCompletedError(ParkingError):
    pass


class InvalidChargingSpotError(ParkingError):
    pass


class ChargingAlreadyActiveError(ParkingError):
    pass


class ChargingNotStartedError(ParkingError):
    pass


class SpotOccupiedError(ParkingError):
    pass


class InvalidRateError(ParkingError):
    pass


class ValidationError(ParkingError):
    pass