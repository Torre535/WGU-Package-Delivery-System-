
# Author: David Torres
# C950 Project
# Student ID: 010779309

import csv
from ArrayDataStructure import ArrayDataStructure
from Package import Package
from CsvReaderHelperFile import get_distance_data_csv, get_address_data_csv, upload_package_data_csv


# The main purpose of this method is to be able to add the raw data from teh CSV to our Array Data structure.
def add_package_data_to_array(filename, package_list):
    """
    This reads package info from the CSV file and adds it to a package list data structure in order to deliver them.

    :param filename: The file name of the CSV file containing package info.
    :param package_list: The ArrayDataStructure is where the data will be added to
    """
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) == 8:
                    package_id, address, city, state, zip, deadline_time, weight, status = row
                    package_obj = Package(int(package_id), address, city, state, zip, deadline_time, float(weight),
                                          "At Hub")
                    package_list.insert_to_array(int(package_id), package_obj)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# The purpose of this is to load distance data from CSV
distance_Info_csv = get_distance_data_csv("CSV Data Files From WGU/WGU C950 Distance Info.csv")

# The purpose of this is to load address data from CSV
address_Info_csv = get_address_data_csv("CSV Data Files From WGU/WGU C950 Address Info.csv")

# The purpose of this is to load package data from CSV
pacakge_info_csv = upload_package_data_csv("CSV Data Files From WGU/WGU C950 Package Info.csv")

# The purpose of this is to create an Array Data structure
Array_data_ = ArrayDataStructure()

# the purpose of this is to load packages into Array
add_package_data_to_array("CSV Data Files From WGU/WGU C950 Package Info.csv", Array_data_)
