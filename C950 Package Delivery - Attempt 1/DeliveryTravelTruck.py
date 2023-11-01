# Author: David Torres
# C950 Project
# Student ID: 010779309


# DeliveryTruck class to represent trucks that will be delivering packages
import datetime


class DeliveryTravelTruck:
    # Constructor to initialize truck attributes
    def __init__(self, capacity, speed, packages, mileage, location, depart_time):
        self.capacity = capacity  # Maximum package capacity for the truck which is 16 in our case
        self.speed = speed  # Speed of the truck which can only be 18 in our case
        self.packages = packages  # The actual packages assigned to the truck
        self.mileage = mileage  # Mileage of the truck driven from the hub
        self.address = location  # Current location or address of the truck
        self.depart_time = depart_time  # Departure time of the truck, 4001 South 700 East is the hub.
        self.time = depart_time  # Current time of the truck leaving the hub

    # String form of a DeliveryTruck object
    def __str__(self):
        return f"Capacity: {self.capacity}, " \
               f"Speed: {self.speed}, " \
               f"Packages: {self.packages}, " \
               f"Mileage: {self.mileage}, " \
               f"Address: {self.location}, " \
               f"Departure Time: {self.depart_time}, " \
               f"Current Time: {self.time}"


manual_load_method = [
    {
        "capacity": 16,  # No more than 16 packages can be on a single truck at once
        "speed": 18,   # The truck can only travel at a speed of 18 miles per hour
        "packages": [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],    # Manually loaded the packages
        "mileage": 0.0,   # The starting total milage for this truck
        "location": "4001 South 700 East",  # This is the starting address or hub address for trucks
        "depart_time": datetime.timedelta(hours=8),   # Time the truck leaves
    },
    {
        "capacity": 16,
        "speed": 18,
        "packages": [3, 6, 9, 11, 12, 17, 18, 21, 23, 24, 26, 27, 35, 36, 38],    # Manually loaded the packages
        "mileage": 0.0,   # The starting total milage for this truck
        "location": "4001 South 700 East",
        "depart_time": datetime.timedelta(hours=10, minutes=20),      # Time the truck leaves
    },
    {
        "capacity": 16,   # No more than 16 packages can be on a single truck at once
        "speed": 18,    # The truck can only travel at a speed of 18 miles per hour
        "packages": [2, 4, 5, 6, 7, 8, 10, 22, 25, 28, 32, 33, 39],  # Manually loaded the packages
        "mileage": 0.0,   # The starting total milage for this truck
        "location": "4001 South 700 East",  # This is the starting address or hub address for trucks
        "depart_time": datetime.timedelta(hours=9, minutes=5),        # Time the truck leaves
    },
]

# This is used to create truck objects in order to load them successfully.
trucks = [DeliveryTravelTruck(**params) for params in manual_load_method]

# Assign individual trucks to their specific packages.
truck1, truck2, truck3 = trucks
