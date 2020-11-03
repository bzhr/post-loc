"""Basic routing and declaration of URLs."""

import logging
from urllib import parse

from .settings import GET_REQUEST
from app import views


URLS = [
    {"route": "/", "view": views.HomeView, "type": GET_REQUEST},
    {"route": "/stores", "view": views.StoresView, "type": GET_REQUEST},
    {"route": "/api/stores", "view": views.StoresApiView, "type": GET_REQUEST},
]


class Router:
    """Routing of requests to view classes."""

    def __init__(self):
        self.logger = logging.getLogger('app.router.Router')

    def get_view(self, path, request_type):
        "Gets the data for the requested path."
        self.logger.info("Matching URL to view")
        parsed_path = parse.urlparse(path)
        return self._get_url(parsed_path.path, request_type)

    def _get_url(self, path, request_type):
        "Matching paths with route handlers"
        path_splitted = path.split("/")
        if len(path_splitted) > 1 and path_splitted[1] == "static":
            self.logger.debug("Matched a static file")
            return {
                "route": "/static", "view": views.StaticFileView, "type": GET_REQUEST
            }
        for url in URLS:
            if url["route"] == path and request_type == url["type"]:
                self.logger.debug("Matched {} with {}".format(path, url["view"]))
                return url
        self.logger.debug("Route not found")
        return {"route": None, "view": views.NotExistingView, "type": GET_REQUEST}
