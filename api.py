from flask import Flask, jsonify, request

from facility_manager import FacilityManager


app = Flask(__name__)

manager = FacilityManager()


# ==================================
# HOME
# ==================================

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Smart Parking System API is running",
        "status": "success"
    })


# ==================================
# GET ALL PARKING LOTS
# ==================================

@app.route("/lots", methods=["GET"])
def get_lots():

    lots = manager.get_all_lots()

    return jsonify([
        lot.to_dict()
        for lot in lots
    ])


# ==================================
# GET ALL PARKING SPOTS
# ==================================

@app.route("/spots", methods=["GET"])
def get_spots():

    spots = manager.get_all_spots()

    return jsonify([
        spot.to_dict()
        for spot in spots
    ])


# ==================================
# GET OCCUPANCY SUMMARY
# ==================================

@app.route("/spots/summary", methods=["GET"])
def get_occupancy_summary():

    summary = manager.get_occupancy_summary()

    return jsonify(summary)


# ==================================
# GET ALL VEHICLES
# ==================================

@app.route("/vehicles", methods=["GET"])
def get_vehicles():

    vehicles = manager.get_all_vehicles()

    return jsonify([
        vehicle.to_dict()
        for vehicle in vehicles
    ])


# ==================================
# GET ACTIVE PARKING SESSIONS
# ==================================

@app.route("/parking/active", methods=["GET"])
def get_active_parking():

    sessions = manager.get_active_parking_sessions()

    return jsonify([
        session.to_dict()
        for session in sessions
    ])


# ==================================
# GET ACTIVE CHARGING SESSIONS
# ==================================

@app.route("/charging/active", methods=["GET"])
def get_active_charging():

    sessions = manager.get_active_charging_sessions()

    return jsonify([
        session.to_dict()
        for session in sessions
    ])


# ==================================
# START PARKING
# ==================================

@app.route("/parking/start", methods=["POST"])
def start_parking():

    data = request.get_json()

    license_plate = data.get("plate")
    spot_id = data.get("spot_id")

    session = manager.start_parking(
        license_plate,
        spot_id
    )

    return jsonify({
        "message": "Parking started successfully",
        "session": session.to_dict()
    }), 201


# ==================================
# END PARKING
# ==================================

@app.route("/parking/end", methods=["POST"])
def end_parking():

    data = request.get_json()

    license_plate = data.get("plate")

    session = manager.end_parking(
        license_plate
    )

    return jsonify({
        "message": "Parking ended successfully",
        "session": session.to_dict()
    })


# ==================================
# START EV CHARGING
# ==================================

@app.route("/charging/start", methods=["POST"])
def start_charging():

    data = request.get_json()

    license_plate = data.get("plate")
    spot_id = data.get("spot_id")

    session = manager.start_charging(
        license_plate,
        spot_id
    )

    return jsonify({
        "message": "EV charging started successfully",
        "session": session.to_dict()
    }), 201


# ==================================
# END EV CHARGING
# ==================================

@app.route("/charging/end", methods=["POST"])
def end_charging():

    data = request.get_json()

    license_plate = data.get("plate")
    energy_used = data.get("energy_used")

    session = manager.end_charging(
        license_plate,
        energy_used
    )

    return jsonify({
        "message": "EV charging ended successfully",
        "session": session.to_dict()
    })


# ==================================
# RUN SERVER
# ==================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )