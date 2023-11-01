# Author: David Torres
# C950 Project
# Student ID: 010779309

# This data structure is an array based hash table that stores key values pares while providing hash functionality
# It meets the requirement for being self-adjusting as it automatically adjusts the list to hold values needed.

class ArrayDataStructure:
    def __init__(self, size=50):
        """
        Initializes the array-based hash table with size parameter which is 50.

        :param size: The size of the hash table or buckets.
        """
        self.size = size
        self.data = [None] * self.size

    def hash_key_location(self, key):
        """
        Hashes a key to find its location.

        :param key: The certain key to be hashed.
        :return: The index or bucket location.
        """
        return hash(key) % self.size

    def insert_to_array(self, key, value):
        """
        Adds a key-value pair into the hash table.

        :param key: The specific key to be added.
        :param value: The value associated with that certain key.
        """
        index = self.hash_key_location(key)
        if self.data[index] is None:
            self.data[index] = []
        for i, (existing_key, _) in enumerate(self.data[index]):
            if existing_key == key:
                self.data[index][i] = (key, value)
                return
        self.data[index].append((key, value))

    def gather_from_array(self, key):
        """
        Retrieves the value associated with a given key in the hash table.

        :param key: The key to look up in the hash table.
        :return: The value associated with the key, or None if not found.
        """
        index = self.hash_key_location(key)
        if self.data[index] is not None:
            for existing_key, value in self.data[index]:
                if existing_key == key:
                    return value
        return None

    def remove_from_array(self, key):
        """
        removes a key-value pair from the hash table.

        :param key: The specific key to be deleted.
        """
        index = self.hash_key_location(key)
        if self.data[index] is not None:
            for i, (existing_key, _) in enumerate(self.data[index]):
                if existing_key == key:
                    del self.data[index][i]
                    return

    def __str__(self):
        """
        Returns a string of the hash table.

        :return: A string of the hash table.
        """
        return str(self.data)

