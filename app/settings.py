"""Settings for the Tranquinity code assignment."""

import os
from jinja2 import Environment, FileSystemLoader

PORT = 8001
ALLOWED_HOSTS = "*"
STORES_DATA_FILE_NAME = "stores.json"
POSTCODES_API_URL = "http://api.postcodes.io/postcodes"

# Entry point of the application
# from where things like static folder are resolved
ROOT = os.path.join(os.getcwd(), "app")

env = Environment(loader=FileSystemLoader('static/templates'))

# Request types
GET_REQUEST = "GET"
POST_REQUEST = "POST"
