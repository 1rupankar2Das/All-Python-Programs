# Develop classes for different types of vehicles (car, bike, truck) and a 
# rental management system. Include functionalities like renting, 
# returning, and calculating rental fees.
from datetime import datetime, timedelta

class Vehicle:
    def __init__(self, vehicle_id, make, model, rate_per_day):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.rate_per_day = rate_per_day
        self.is_rented = False
        self.rented_by = None
        self.rent_start_date = None

    def __str__(self):
        return f"Vehicle(id={self.vehicle_id}, make={self.make}, model={self.model}, rate_per_day={self.rate_per_day})"

class Car(Vehicle):
    def __init__(self, vehicle_id, make, model, rate_per_day, number_of_doors):
        super().__init__(vehicle_id, make, model, rate_per_day)
        self.number_of_doors = number_of_doors

class Bike(Vehicle):
    def __init__(self, vehicle_id, make, model, rate_per_day, type_of_bike):
        super().__init__(vehicle_id, make, model, rate_per_day)
        self.type_of_bike = type_of_bike

class Truck(Vehicle):
    def __init__(self, vehicle_id, make, model, rate_per_day, cargo_capacity):
        super().__init__(vehicle_id, make, model, rate_per_day)
        self.cargo_capacity = cargo_capacity

class RentalManagementSystem:
    def __init__(self):
        self.vehicles = []
        self.rentals = {}

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle} added to the system.")

    def rent_vehicle(self, vehicle_id, customer_name, rent_start_date):
        vehicle = self.get_vehicle_by_id(vehicle_id)
        if vehicle:
            if vehicle.is_rented:
                print(f"Vehicle {vehicle_id} is already rented.")
            else:
                vehicle.is_rented = True
                vehicle.rented_by = customer_name
                vehicle.rent_start_date = rent_start_date
                self.rentals[vehicle_id] = {'customer_name': customer_name, 'rent_start_date': rent_start_date}
                print(f"Vehicle {vehicle_id} rented by {customer_name} starting {rent_start_date}.")
        else:
            print(f"No vehicle found with ID {vehicle_id}.")

    def return_vehicle(self, vehicle_id, return_date):
        vehicle = self.get_vehicle_by_id(vehicle_id)
        if vehicle:
            if not vehicle.is_rented:
                print(f"Vehicle {vehicle_id} is not currently rented.")
            else:
                rent_start_date = vehicle.rent_start_date
                rental_days = (return_date - rent_start_date).days
                rental_fee = rental_days * vehicle.rate_per_day
                vehicle.is_rented = False
                vehicle.rented_by = None
                vehicle.rent_start_date = None
                del self.rentals[vehicle_id]
                print(f"Vehicle {vehicle_id} returned on {return_date}. Total rental fee: ${rental_fee}.")
                return rental_fee
        else:
            print(f"No vehicle found with ID {vehicle_id}.")
        return 0

    def get_vehicle_by_id(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

# Example usage
rental_system = RentalManagementSystem()

car1 = Car("C001", "Toyota", "Camry", 50, 4)
bike1 = Bike("B001", "Giant", "Escape 3", 20, "Road Bike")
truck1 = Truck("T001", "Ford", "F-150", 80, 1000)

rental_system.add_vehicle(car1)
rental_system.add_vehicle(bike1)
rental_system.add_vehicle(truck1)

rental_system.rent_vehicle("C001", "Alice", datetime(2024, 5, 1))
rental_system.return_vehicle("C001", datetime(2024, 5, 10))

rental_system.rent_vehicle("B001", "Bob", datetime(2024, 5, 5))
rental_system.return_vehicle("B001", datetime(2024, 5, 6))
