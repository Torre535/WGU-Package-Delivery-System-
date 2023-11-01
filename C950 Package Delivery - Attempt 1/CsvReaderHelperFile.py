# Author: David Torres
# C950 Project
# Student ID: 010779309

import csv


# This class is used as a helper function to be able to open and read data from CSV.
def load_csv_data(filename):
    """
    reads a CSV file and returns its data

    :param filename: The name of the CSV file
    :return: list containing the CSV data.
    """
    data = []
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        data = list(csv_reader)
    return data


def append_to_csv(filename, data):
    """
    Appends data to a CSV file when needed.

    :param filename: The name of the CSV file to append data to.
    :param data: To append to the CSV file.
    """
    with open(filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)


def get_distance_data_csv(filename):
    """
    Gathers distance from a CSV file.

    :param filename: CSV file containing distance data.
    :return: Lists containing distance data.
    """
    return load_csv_data(filename)


def get_address_data_csv(filename):
    """
    Gathers address data from a CSV file data.

    :param filename: CSV file containing address data.
    :return: Lists containing address data.
    """
    return load_csv_data(filename)


def upload_package_data_csv(filename):
    """
     Uploads package data from a CSV file.

    :param filename: CSV file containing package data.
    :return: Lists containing package data.
    """
    return load_csv_data(filename)
