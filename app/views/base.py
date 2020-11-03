"""Base classes for JSON and HTML views."""


from os import path
import json
import logging
from jinja2 import TemplateNotFound

from ..settings import env


class BaseView:
    """Base view exposing a render method."""

    def __init__(self, request):
        self.path = request.path
        self.data = self.get_data()

    def render():
        raise NotImplementedError("View classes must implement a render method")

    def get_data(self):
        pass


class HtmlView(BaseView):
    """
    Renders a HTML template.
    Defines a template attribute with the name of the template.
    """

    template = None
    data = None
    headers = ("Content-type", "text/html; charset=utf-8")
    logger = logging.getLogger("app.views.base.HtmlView")

    def render(self):
        "The render method uses Jinja2 to load and render the template."
        if not self.template:
            self.logger.error("Template file needs to be set as attribute")
            raise ValueError("Template file needs to be set as attribute")
        try:
            template = env.get_template(self.template)
            self.logger.info("Rendering HTML template")
            return template.render(data=self.data).encode()
        except TemplateNotFound:
            self.logger.error("Template file doesn't exist")
            raise ValueError("Template file doesn't exist")


class JsonView(BaseView):
    headers = ('Content-type', 'application/json')

    def render(self):
        data = self.get_data()
        return json.dumps(data).encode('utf-8')


class StaticFileView(BaseView):

    # file_types = {
    #     "images": {
    #         "types": ["ico", "png", "jpg", "webp"],
    #         "header": ("Content-type", "image/x-icon")
    #     },
    #     "manifest": {
    #         "types": ["json"],
    #         "header": ("Content-type", "application/manifest+json")
    #     }
    # }
    headers = ("Content-type", "image/x-icon")
    logger = logging.getLogger("app.views.base.StaticFileView")

    def render(self):
        self.relative_path = self._get_relative_path()
        if not path.isfile(self.relative_path):
            self.logger.error(
                "File path doesn't exist path: {}".format(self.relative_path)
            )
            raise ValueError("File doesn't exist")
        with open(self.relative_path, 'rb') as file:
            self.logger.info("Reading file: {}".format(self.relative_path))
            return file.read()

    def _get_relative_path(self):
        "Remove slash from URL path, to read the file as a relative path"
        if self.path[0] == "/":
            return self.path[1:]
        else:
            return self.path
