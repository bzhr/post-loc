"""Special purpose views, that build on the base views."""

from urllib import parse
import logging

from .base import HtmlView, JsonView
from ..postcodes import Stores


class HomeView(HtmlView):
    """Home view"""

    template = "index.html"


class NotExistingView(HtmlView):
    """Nonexistent 404 view"""

    template = "404.html"


class StoresView(HtmlView):
    """Stores view"""

    template = "stores.html"

    def get_data(_):
        stores = Stores()
        stores.get_api_data()
        stores.merge_data()
        return stores.data


class StoresApiView(JsonView):
    """Stores API JSON view"""

    query_string = None
    stores = None
    logger = logging.getLogger("app.views.main.StoresApiView")

    def parse_query_string(self):
        self.logger.info("Parsing query string")
        parsed_path = parse.urlparse(self.path)
        self.query_string = parse.parse_qs(parsed_path.query)

    def get_data(self):
        self.logger.info("Preparing API data")
        self.stores = Stores()
        self.parse_query_string()
        query = self.query_string.get("q")
        if query:
            self.logger.info("Returning filtered data")
            self.logger.debug("Query string: {}".format(query))
            data = (
                self.filter_data(query, "postcode") +
                sorted(self.filter_data(query, "name"), key=lambda k: k['name'])
            )
            return self.paginate(data)
        self.logger.info("Returning all data")
        return self.paginate(self.stores.data)

    def filter_data(self, query, key):
        """
        Query - list of query strings, key - on which key to filter.
        The search is case insensitive
        """
        filtered_data = [
            x for x in self.stores.data
            if any(y in x[key].lower() for y in query)
        ]
        return filtered_data

    def paginate(self, data):
        self.logger.info("Paginating data")
        # Either use offset from the query string
        # Or start from index 0
        offset_query = self.query_string.get("offset", [0])
        offset = int(offset_query[0])
        # Either use providded query string limit
        # Or use full length of the data
        limit_query = self.query_string.get("limit", [len(data)])
        limit = int(limit_query[0])
        self.logger.debug("Paginate limit: {}, offset: {}".format(limit, offset))
        return data[offset: limit]
