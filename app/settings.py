"""Settings for the Tranquinity code assignment."""

import os
from jinja2 import Environment, FileSystemLoader


# Port on which the app will run
PORT = 8001
# Use (*) allow all hosts. In order to escape CORS errors.
ALLOWED_HOSTS = "*"
# This is the json file with the stores/postcodes data
STORES_DATA_FILE_NAME = "stores.json"
# This is the API endpoint that returns data for postcodes.
POSTCODES_API_URL = "http://api.postcodes.io/postcodes"

# Entry point of the application or root directory
# from where things like static folder are resolved
ROOT = os.path.join(os.getcwd(), "app")

# Templates loader
env = Environment(loader=FileSystemLoader('static/templates'))

# Request types
GET_REQUEST = "GET"
