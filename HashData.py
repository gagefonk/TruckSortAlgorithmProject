import csv
import os
from Package import Package


class HashData:
    # Constructor
    def __init__(self):
        path = os.getcwd()
        file_name = "/WGUPS Package File.csv"
        self.total_packages = self.get_csv_len(path, file_name)
        self.packages = []
        for i in range(self.total_packages):
            self.packages.append([])
        self.parse_csv(path, file_name)

    # get the hash key
    def get_hash(self, key):
        return key % self.total_packages

    # add package to packages hash map
    def add(self, key, package):
        self.packages[key] = package

    # delete package from packages hash map
    def delete(self, id):
        key = self.get_hash(id)
        self.packages.remove(key)

    # insert package into hash map
    def insert(self, id, address, city, state, zip, deadline, weight, status):
        delivery = Package(id, address, city, state, zip, deadline, weight, status, '')
        key = self.get_hash(id)
        self.packages[key] = delivery

    # lookup package from hash map
    def lookup(self, id):
        key = self.get_hash(id)
        return self.packages[key]

    # read package data from csv to hash map
    def parse_csv(self, path, file_name):
        with open(path + file_name) as file:
            reader = csv.reader(file, delimiter=',')
            next(reader, None)  # skip headers
            for row in reader:
                delivery = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], "AT_HUB", row[7])
                key = self.get_hash(delivery.get_package_id())
                self.add(key, delivery)

    # grab length for hash map size
    def get_csv_len(self, path, file_name):
        with open(path + file_name) as file:
            reader = csv.reader(file, delimiter=',')
            next(reader, None)  # skip headers
            return len(list(reader))
