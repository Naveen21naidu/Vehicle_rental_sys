# Vehicle Rental System

A simple Vehicle Rental System built using Object-Oriented Programming (OOP) concepts in Python.

## Features
- View available vehicles
- Rent a vehicle for a specific number of days
- Return rented vehicles
- Pricing varies based on vehicle type and attributes

## OOP Concepts Used
- **Encapsulation** – Private availability status in Vehicle class
- **Inheritance** – Car and Bike inherit from Vehicle
- **Polymorphism** – Different rent calculation logic for Car
- **Composition** – Customer interacts with Vehicle

## Classes Overview
- `Vehicle` → Base class (common properties like name, brand, rent)
- `Car` → Derived class (adds seats, fuel type, custom pricing)
- `Bike` → Derived class (adds engine capacity)
- `Customer` → Handles renting and returning vehicles
- `RentalSystem` → Manages vehicles and user interactions

## How to Run
```bash
python vehicle_rental_system.py
