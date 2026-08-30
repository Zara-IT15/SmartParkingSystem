# Smart Parking Lot & EV Charging Station Management System

## Project Overview

The Smart Parking Lot & EV Charging Station Management System is a Python-based backend system designed to manage parking lots, parking spaces, vehicles, parking sessions, and EV charging sessions.

The system provides both:

- A Command-Line Interface (CLI)
- A REST API using Flask

The system stores application data in JSON files.

## Objectives

The main objectives of this project are:

- Manage multiple parking lots.
- Add and manage different types of parking spots.
- Register vehicles.
- Start and end parking sessions.
- Calculate parking fees.
- Manage EV charging sessions.
- Calculate EV charging fees based on energy consumption.
- Display parking occupancy information.
- Store data using JSON files.
- Provide REST API endpoints.
- Handle invalid input and errors.

## Features

### Parking Management

- Add parking lots.
- Add parking spots.
- Support Regular, Handicapped, and EV parking spots.
- Track parking spot availability.
- Track occupied and available spots.

### Vehicle Management

- Register vehicles.
- Store vehicle plate number.
- Store owner name.
- Store vehicle type.
- Store registration date.

### Parking Sessions

- Start parking for a registered vehicle.
- End an active parking session.
- Store check-in and check-out times.
- Calculate parking fees.
- Track active parking sessions.

### EV Charging

- Start EV charging.
- End EV charging.
- Record energy consumption in kWh.
- Calculate charging fees.
- Track active charging sessions.

### Occupancy Summary

The system provides:

- Total parking spots
- Available spots
- Occupied spots
- Out-of-service spots
- Regular spots
- Handicapped spots
- EV spots

### REST API

The project provides REST API endpoints using Flask.

The API supports:

- Parking lot information
- Parking spot information
- Occupancy summary
- Vehicle information
- Parking operations
- EV charging operations
- Active session information

### Error Handling

The API handles errors such as:

- Parking spot not found
- Vehicle not found
- Parking spot unavailable
- Missing required data
- Invalid energy input
- No active parking session
- No active charging session

## Technologies Used

- Python
- Flask
- REST API
- JSON
- Object-Oriented Programming
- UUID
- Git
- GitHub

## Project Structure

SmartParkingSystem/

    api.py
    main.py
    facility_manager.py
    exceptions.py
    requirements.txt
    README.md

    data/
        lots.json
        spots.json
        vehicles.json
        parking_sessions.json
        charging_sessions.json

    models/
        parking_lot.py
        parking_spot.py
        vehicle.py
        parking_session.py
        charging_session.py

## Models

### ParkingLot

Represents a parking facility.

Stores:

- Lot ID
- Lot name
- Location

### ParkingSpot

Represents an individual parking space.

Stores:

- Spot ID
- Lot ID
- Spot type
- Status
- Hourly parking rate
- EV kWh rate

### Vehicle

Represents a registered vehicle.

Stores:

- Vehicle plate
- Owner name
- Vehicle type
- Registration date

### ParkingSession

Represents a parking session.

Stores:

- Session ID
- Vehicle plate
- Spot ID
- Lot ID
- Check-in time
- Check-out time
- Parking fee
- Session status

### ChargingSession

Represents an EV charging session.

Stores:

- Session ID
- Vehicle plate
- EV spot ID
- Start time
- End time
- Energy used
- Charging fee
- Session status

## Data Storage

The system uses JSON files for persistent data storage.

Data files:

- data/lots.json
- data/spots.json
- data/vehicles.json
- data/parking_sessions.json
- data/charging_sessions.json

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Zara-IT15/SmartParkingSystem.git