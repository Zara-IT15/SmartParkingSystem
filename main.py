from facility_manager import FacilityManager


def show_menu():
    print()
    print("==============================")
    print("     SMART PARKING SYSTEM")
    print("==============================")
    print("1. Add Parking Lot")
    print("2. Add Parking Spot")
    print("3. Register Vehicle")
    print("4. Start Parking")
    print("5. End Parking")
    print("6. Start EV Charging")
    print("7. End EV Charging")
    print("8. View Parking Spots")
    print("9. View Vehicles")
    print("10. View Active Parking Sessions")
    print("11. View Active Charging Sessions")
    print("0. Exit")
    print("==============================")


def main():
    manager = FacilityManager()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        try:

            # --------------------------------
            # 1. ADD PARKING LOT
            # --------------------------------
            if choice == "1":
                lot_id = input("Enter lot ID: ").strip()
                name = input("Enter lot name: ").strip()
                location = input("Enter location: ").strip()

                lot = manager.add_lot(
                    lot_id,
                    name,
                    location
                )

                print()
                print("Parking lot added successfully.")
                print(lot.to_dict())

            # --------------------------------
            # 2. ADD PARKING SPOT
            # --------------------------------
            elif choice == "2":
                spot_id = input("Enter spot ID: ").strip()
                lot_id = input("Enter lot ID: ").strip()

                spot_type = input(
                    "Enter spot type (REGULAR/HANDICAPPED/EV): "
                ).strip().upper()

                hourly_rate = float(
                    input("Enter hourly rate: ")
                )

                kwh_rate = 0

                if spot_type == "EV":
                    kwh_rate = float(
                        input("Enter kWh rate: ")
                    )

                spot = manager.add_spot(
                    spot_id,
                    lot_id,
                    spot_type,
                    hourly_rate,
                    kwh_rate
                )

                print()
                print("Parking spot added successfully.")
                print(spot.to_dict())

            # --------------------------------
            # 3. REGISTER VEHICLE
            # --------------------------------
            elif choice == "3":
                license_plate = input(
                    "Enter vehicle plate: "
                ).strip()

                owner_name = input(
                    "Enter owner name: "
                ).strip()

                vehicle_type = input(
                    "Enter vehicle type (CAR/MOTORCYCLE/EV_CAR): "
                ).strip().upper()

                vehicle = manager.register_vehicle(
                    license_plate,
                    owner_name,
                    vehicle_type
                )

                print()
                print("Vehicle registered successfully.")
                print(vehicle.to_dict())

            # --------------------------------
            # 4. START PARKING
            # --------------------------------
            elif choice == "4":
                license_plate = input(
                    "Enter vehicle plate: "
                ).strip()

                spot_id = input(
                    "Enter parking spot ID: "
                ).strip()

                session = manager.start_parking(
                    license_plate,
                    spot_id
                )

                print()
                print("Parking started successfully.")
                print(session.to_dict())

            # --------------------------------
            # 5. END PARKING
            # --------------------------------
            elif choice == "5":
                license_plate = input(
                    "Enter vehicle plate: "
                ).strip()

                session = manager.end_parking(
                    license_plate
                )

                print()
                print("Parking ended successfully.")
                print(session.to_dict())

            # --------------------------------
            # 6. START EV CHARGING
            # --------------------------------
            elif choice == "6":
                license_plate = input(
                    "Enter EV vehicle plate: "
                ).strip()

                spot_id = input(
                    "Enter EV spot ID: "
                ).strip()

                session = manager.start_charging(
                    license_plate,
                    spot_id
                )

                print()
                print("Charging started successfully.")
                print(session.to_dict())

            # --------------------------------
            # 7. END EV CHARGING
            # --------------------------------
            elif choice == "7":
                license_plate = input(
                    "Enter EV vehicle plate: "
                ).strip()

                energy_used = float(
                    input("Enter energy used in kWh: ")
                )

                session = manager.end_charging(
                    license_plate,
                    energy_used
                )

                print()
                print("Charging ended successfully.")
                print(session.to_dict())

            # --------------------------------
            # 8. VIEW PARKING SPOTS
            # + OCCUPANCY SUMMARY
            # --------------------------------
            elif choice == "8":
                print()
                print("--- PARKING SPOTS ---")

                spots = manager.get_all_spots()

                if not spots:
                    print("No parking spots found.")
                else:
                    for spot in spots:
                        print(spot.to_dict())

                print()
                print("--- OCCUPANCY SUMMARY ---")

                summary = manager.get_occupancy_summary()

                print(
                    "Total Spots:",
                    summary["total_spots"]
                )

                print(
                    "Available Spots:",
                    summary["available_spots"]
                )

                print(
                    "Occupied Spots:",
                    summary["occupied_spots"]
                )

                print(
                    "Out of Service:",
                    summary["out_of_service_spots"]
                )

                print(
                    "Regular Spots:",
                    summary["regular_spots"]
                )

                print(
                    "Handicapped Spots:",
                    summary["handicapped_spots"]
                )

                print(
                    "EV Spots:",
                    summary["ev_spots"]
                )

            # --------------------------------
            # 9. VIEW VEHICLES
            # --------------------------------
            elif choice == "9":
                print()
                print("--- VEHICLES ---")

                vehicles = manager.get_all_vehicles()

                if not vehicles:
                    print("No vehicles registered.")
                else:
                    for vehicle in vehicles:
                        print(vehicle.to_dict())

            # --------------------------------
            # 10. ACTIVE PARKING SESSIONS
            # --------------------------------
            elif choice == "10":
                print()
                print("--- ACTIVE PARKING SESSIONS ---")

                sessions = manager.get_active_parking_sessions()

                if not sessions:
                    print("No active parking sessions.")
                else:
                    for session in sessions:
                        print(session.to_dict())

            # --------------------------------
            # 11. ACTIVE CHARGING SESSIONS
            # --------------------------------
            elif choice == "11":
                print()
                print("--- ACTIVE CHARGING SESSIONS ---")

                sessions = manager.get_active_charging_sessions()

                if not sessions:
                    print("No active charging sessions.")
                else:
                    for session in sessions:
                        print(session.to_dict())

            # --------------------------------
            # 0. EXIT
            # --------------------------------
            elif choice == "0":
                print()
                print("Thank you for using Smart Parking System.")
                break

            # --------------------------------
            # INVALID CHOICE
            # --------------------------------
            else:
                print()
                print("Invalid choice. Please try again.")

        except Exception as error:
            print()
            print("Error:", error)


if __name__ == "__main__":
    main()