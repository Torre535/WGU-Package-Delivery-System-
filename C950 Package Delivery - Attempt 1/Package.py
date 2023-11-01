# Author: David Torres
# C950 Project
# Student ID: 010779309

# Package class to represent packages for delivery by trucks
class Package:
    # Constructor method in order to make a package object.
    # This contains all the attributes needed to deliver a package
    def __init__(self, ID, address, city, state, zip, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery_time = None
        self.departure_time = None

    # String form of a Package object
    def __str__(self):
        return f"Package ID: {self.ID}, " \
               f"Address: {self.address}, " \
               f"City: {self.city}, " \
               f"State: {self.state}, " \
               f"Zip Code: {self.zip}, " \
               f"Deadline: {self.deadline}, " \
               f"Weight: {self.weight}, " \
               f"Status: {self.status}, " \
               f"Delivery Time: {self.delivery_time}, " \
 \
 \
    # this method is used if there are any updates on address by the sender
    def update_address(self, new_address):
        """
       This method is used to update the address of the package. This method is mainly used for package #9.

        :param new_address: The new address to be assigned to the package.
        """
        self.address = new_address
