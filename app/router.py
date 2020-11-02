"""Basic routing and declaration of URLs."""

from urllib import parse

from .settings import GET_REQUEST
from .views import main as main_views
from .views.base import StaticFileView


URLS = [
    {"route": "/", "view": main_views.HomeView, "type": GET_REQUEST},
    {"route": "/stores", "view": main_views.StoresView, "type": GET_REQUEST},
    {"route": "/api/stores", "view": main_views.StoresApiView, "type": GET_REQUEST},
]


class Router:
    """Routing of requests to view classes."""

    def get_view(self, path, request_type):
        "Gets the data for the requested path."
        parsed_path = parse.urlparse(path)
        return self._get_url(parsed_path.path, request_type)

    def _get_url(_, path, request_type):
        "Matching paths with route handlers"
        path_splitted = path.split("/")
        if len(path_splitted) > 1 and path_splitted[1] == "static":
            return {"route": "/static", "view": StaticFileView, "type": GET_REQUEST}
        for url in URLS:
            if url["route"] == path and request_type == url["type"]:
                return url
        return {"route": None, "view": main_views.NotExistingView, "type": GET_REQUEST}
