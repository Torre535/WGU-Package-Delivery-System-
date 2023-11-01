# Author: David Torres
# C950 Project
# Student ID: 010779309

from LoadingDataToArray import add_package_data_to_array, Array_data_, distance_Info_csv, address_Info_csv
import tkinter as tk
from tkinter import simpledialog, messagebox
import datetime
from DeliveryTravelTruck import truck1, truck2, truck3
from ArrayDataStructure import ArrayDataStructure


# Method for finding distance between two addresses. Used in the algo to find next address to travel to.
def calculate_distance_for_decision_making(x_index, y_index, distance_info, address_info):
    """
   This allows for the math to be done to find the distance between two addresses using their indices.

   :param x_index: The index of the first address in distance_info.
   :param y_index: The index of the second address in distance_info.
   :param distance_info: The list containing distance data.
   :param address_info: The list containing address data.
   :return: The calculated distance
   """
    try:
        # Gathers the distance from the distance_data list
        distance = distance_info[x_index][y_index]

        # If the distance value is an empty, swap indices to try again
        if isinstance(distance, str) and distance.strip() == '':
            distance = distance_info[y_index][x_index]

        # Convert the distance
        return float(distance)
    except (ValueError, IndexError):
        print("Error: Invalid address indices or distance data format.")
        return None


# Defines the list of trucks that are used to deliver packages from the hub
trucks = [truck1, truck2, truck3]


def parcel_delivery_method(delivery_truck, Array_data_, CSV_Distance_Data, CSV_Address_Data, current_time):
    """
   This is the actual delivery method process done by each truck.

   :param delivery_truck: The truck for delivering.
   :param Array_data_: The data structure containing packages.
   :param CSV_Distance_Data: Distance data in CSV format.
   :param CSV_Address_Data: Address data in CSV format.
   :param current_time: The current time as a datetime.timedelta.
   """
    # Dictionary to map addresses to their corresponding address numbers
    address_dictionary_to_map = {row[2]: int(row[0]) for row in CSV_Address_Data}

    # Add packages on the truck
    pending_delivery_packages = set(delivery_truck.packages)

    # Initialize the delivery address
    current_address = delivery_truck.address

    # Initialize the mileage to track the distance traveled by the truck
    total_mileage = 0.0

    delivery_truck.packages.clear()

    while pending_delivery_packages:
        # Initialize variables to find the nearest package route
        closest_distance_on_route = float('inf')
        closest_package_on_route = None

        # Iterate through the undelivered packages to find the nearest address
        for package_id in pending_delivery_packages:
            package = Array_data_.gather_from_array(package_id)
            package_address = package.address

            # Check if the current time is 10:20:00 and the package is #9
            if package_id == 9 and current_time == datetime.timedelta(hours=10, minutes=20, seconds=0):
                # Update the address of package #9
                package.update_address("410 S State St")

            # Calculate the distance between the current address and the package's address
            distance = calculate_distance_for_decision_making(
                address_dictionary_to_map.get(current_address, None),
                address_dictionary_to_map.get(package_address, None),
                CSV_Distance_Data, CSV_Address_Data
            )

            # Checks to see if the current package is closer than the previous package
            if distance < closest_distance_on_route:
                closest_distance_on_route = distance
                closest_package_on_route = package

        # If a nearest package is found, update the truck route
        if closest_package_on_route:
            # Add the nearest package to the truck
            delivery_truck.packages.append(closest_package_on_route.ID)

            # Remove the delivered packages
            pending_delivery_packages.remove(closest_package_on_route.ID)

            # Update the total mileage traveled
            total_mileage += closest_distance_on_route

            # Update current address and mileage
            current_address = closest_package_on_route.address
            delivery_truck.address = current_address
            delivery_truck.mileage = total_mileage

            # Update delivery time based on distance and speed form the truck
            delivery_truck.time += datetime.timedelta(hours=closest_distance_on_route / delivery_truck.speed)

            # Update delivery and departure times by the truck
            closest_package_on_route.delivery_time = delivery_truck.time
            closest_package_on_route.departure_time = delivery_truck.depart_time


# Get the current time as a datetime.timedelta
current_time = datetime.timedelta(hours=10, minutes=20, seconds=0)

# Iterate through the list of trucks and process their deliveries until finished
for delivery_truck in trucks:
    parcel_delivery_method(delivery_truck, Array_data_, distance_Info_csv, address_Info_csv, current_time)


class PackageDeliveryAppDisplay:
    """
   This class represents a graphical user interface (GUI) for a package delivery system. It allows users to interact
   with the system as a popup window, view package details for single or all 40, and calculate mileage.
   """

    def __init__(self, root):

        """
        Initializes the user interface (GUI)

        :param root: The main GUI window popup
        """
        self.root = root   # This assigns the root parameter to access GUI
        self.root.title("Package Delivery System")  # The title of the Popup display
        self.root.geometry("200x200")  # Sets the dimensions for the popup
        self.create_popup_window()   # Creates the popup window
        self.truck1_mileage = truck1.mileage   # Assign miles
        self.truck2_mileage = truck2.mileage    # Assign miles
        self.truck3_mileage = truck3.mileage     # Assign miles

        self.create_widgets_popup()

    def create_popup_window(self):
        """
      Creates a popup window in the center of the users screen.
      """
        # Used to determine the sizing for the popup window that the user interacts with
        screen_width_data = self.root.winfo_screenwidth()
        screen_height_data = self.root.winfo_screenheight()

        # These are the x and y coordinates to center the window to make it readable
        x = (screen_width_data - 800) // 3
        y = (screen_height_data - 600) // 3

        # Set the window's position on the users screen
        self.root.geometry(f"800x600+{x}+{y}")

    def create_widgets_popup(self):
        """
        Creates the GUI widgets, including labels and buttons.
        """
        tk.Label(self.root, text="WGU Package Delivery System!", font=("Times New Roman", 15)).pack(pady=20)

        tk.Button(self.root, text="Total Combined Mileage for All Trucks", command=self.calculate_total_mileage,
                  font=("Times New Roman", 12)).pack()
        tk.Button(self.root, text="Search for an Single Package Only", command=self.search_for_single_package,
                  font=("Times New Roman", 12)).pack()
        tk.Button(self.root, text="Search for All 40 Packages at a Specific Time",
                  command=self.find_total_packages_details_at_time, font=("Times New Roman", 12)).pack()
        tk.Button(self.root, text="Exit", command=self.root.quit, font=("Times New Roman", 12)).pack()

    def calculate_total_mileage(self):
        """
        Calculates and displays the total combined mileage for all trucks to the user.
        """
        total_traveled_mileage = self.truck1_mileage + self.truck2_mileage + self.truck3_mileage

        messagebox.showinfo("Total Mileage", f"The total mileage for all trucks is: {total_traveled_mileage} miles")

    def search_for_single_package(self):
        """
        The user can search for a single package by ID and check its status at a specific time.
        """
        try:
            user_data_input = simpledialog.askstring("Package ID", "Enter the numeric package ID number:",
                                                     parent=self.root)

            # Check if user_data_input is empty and then give them a warning
            if user_data_input is not None:
                package_id = int(user_data_input)
                user_time = simpledialog.askstring("Package Time",
                                                   "Please enter a time to check package status (HH:MM:SS):",
                                                   parent=self.root)
                (h, m, s) = user_time.split(":")
                form_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                # Locate the specific package by ID
                package = Array_data_.gather_from_array(package_id)

                if package is not None:
                    # Update package location based on the provided time by the user
                    package.status = "Delivered" if package.delivery_time < form_timedelta else \
                        "En route" if package.departure_time > form_timedelta else "At Hub"

                    # Create a message with package details to be displayed to the user
                    message = f"Package {package.ID} details:\n{str(package)}"

                    # Display the package details in a message box that pops up
                    messagebox.showinfo("Package Details", message)
                else:
                    messagebox.showerror("Package Not Found", f"Package with ID {package_id} not found.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Invalid package ID or time format. Please try again.")

    def find_total_packages_details_at_time(self):
        """
        The user can search for all 40 packages and check their statuses at a specific time.
        """
        try:
            time_search = simpledialog.askstring("Search For Time",
                                                 "Please enter a time to check the status of all packages (HH:MM:SS):",
                                                 parent=self.root)
            if time_search is not None:
                (h, m, s) = time_search.split(":")
                form_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                # Create a list to store package details to display to user
                package_details = []

                # Iterate through all packages and gather all 40 packages
                for package_id in range(1, 41):
                    package = Array_data_.gather_from_array(package_id)

                    # Update the package's status based on the time
                    if package.delivery_time < form_timedelta:
                        package.status = "Delivered"
                    elif package.departure_time > form_timedelta:
                        package.status = "En route"
                    else:
                        package.status = "At Hub"

                    package_info = f"Package {package.ID}: {str(package)}"
                    package_details.append(package_info)

                # Construct a large message by joining the package details to display
                message = "\n".join(package_details)

                # Display the package details in a message box pop up window
                messagebox.showinfo("All Packages Details", message)
        except ValueError:
            messagebox.showerror("Invalid Input", "Invalid time format. Please try again.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PackageDeliveryAppDisplay(root)
    root.mainloop()
