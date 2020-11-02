"""Special purpose views, that build on the base views."""

from urllib import parse

from .base import HtmlView, JsonView
from ..postcodes import Stores


class HomeView(HtmlView):
    template = "index.html"


class NotExistingView(HtmlView):
    template = "404.html"


class StoresView(HtmlView):
    template = "stores.html"

    def get_data(_):
        stores = Stores()
        stores.get_api_data()
        stores.merge_data()
        return stores.data


class StoresApiView(JsonView):
    query_string = None
    stores = None

    def parse_query_string(self):
        parsed_path = parse.urlparse(self.path)
        self.query_string = parse.parse_qs(parsed_path.query)

    def get_data(self):
        self.stores = Stores()
        self.parse_query_string()
        query = self.query_string.get("q")
        if query:
            return (
                self.filter_data(query, "postcode") +
                sorted(self.filter_data(query, "name"), key=lambda k: k['name'])
            )
        return self.stores.data

    def filter_data(self, query, key):
        """
        Query - list of query strings, key - on which key to filter.
        The search is case insensitive
        """
        filtered_data = [
            x for x in self.stores.data
            if any(y in x[key].lower() for y in query)
        ]
        # TODO if key is name, sort the list by name
        return filtered_data
