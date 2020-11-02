"""Helpers for getting info on postcodes and operations for the stores data."""

import json
import requests
from os.path import join, exists
from geopy.distance import distance

from . import settings


class Stores:
    """
    This class manages all operations with the stores.json file.
    """

    def __init__(self):
        self.file_path = join("static/data/", settings.STORES_DATA_FILE_NAME)
        if not exists(self.file_path):
            raise ValueError("Data file does not exist")
        self.data = self.read_data_file()
        self.api_data = None

    def read_data_file(self):
        "Reads the JSON file to a Python list"
        with open(self.file_path) as json_file:
            data = json.load(json_file)
        return data

    def get_api_data(self):
        "Gets postcode info for each postcode from postcodes.io API"
        post_codes = [x["postcode"] for x in self.data]
        post_data = dict(postcodes=post_codes)
        r = requests.post(settings.POSTCODES_API_URL, data=post_data)
        if not r.status_code == 200 and r.json()['result'] == 200:
            raise Exception("Failed to retreive postcodes from the API")
        self.api_data = r.json()["result"]

    def merge_data(self):
        "Merge the results from the API to the data from the local file."
        print("API data length: ", len(self.api_data))
        for index, item in enumerate(self.data):
            result = self.api_data[index]['result']
            if result:
                item['latitude'] = self.api_data[index]['result']['latitude']
                item['longitude'] = self.api_data[index]['result']['longitude']
            else:
                # TODO replace print with logging
                print("No result for:", self.api_data[index]['query'])

    def measure_distance(self, point_a, point_b):
        "Measure the distance between two lat/long coordinates tuples in km"
        return distance(point_a, point_b).km

    def stores_within_radius(self, radius, postcode):
        "Filter all stores that are within a distance (radius) from a given postcode"
        if not type(radius) == int or type(radius) == float:
            raise ValueError("Radius needs to be a number")
        if radius <= 0:
            raise ValueError("Radius needs to be a positive number")
        if radius > 6371:
            raise ValueError("Maximum radius is 6371")

        self.setup_data()

        item_a_list = [x for x in self.data if x["postcode"] == postcode]
        if item_a_list and len(item_a_list) == 1:
            item_a = item_a_list[0]
        else:
            raise ValueError("Post Code is not found in the list")
        print("Item a: ", item_a)
        if "latitude" not in item_a.keys():
            raise ValueError(
                "Latitude/Longitude coordinates not found for {}".format(postcode)
            )
        return sorted(
            [
                item_b for item_b in self.data
                if "latitude" in item_b.keys()
                and self.measure_distance(
                    self.create_coordinates_tuple(item_a),
                    self.create_coordinates_tuple(item_b),
                ) <= radius
            ],
            key=lambda k: k['latitude'],
            reverse=True
        )

    def create_coordinates_tuple(self, item):
        "Create a lat/long coordinates tuple."
        if "latitude" not in item.keys() or "longitude" not in item.keys():
            raise ValueError("Item is missing the coordinates")
        return item["latitude"], item["longitude"]

    def setup_data(self):
        "Setup the data, so that the API call is only made once"
        if not self.api_data:
            self.get_api_data()
            self.merge_data()
