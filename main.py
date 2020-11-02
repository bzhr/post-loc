import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus

from app import settings
from app.router import Router


router = Router()


class _RequestHandler(BaseHTTPRequestHandler):
    """
    The RequestHandler is the main point of the application.
    The Request handler ties the different parts of the web server together.
    """

    def _set_headers(self, headers):
        self.send_response(HTTPStatus.OK.value)
        key, value = headers
        self.send_header(key, value)
        # Allow requests from any origin, so CORS policies don't
        # prevent local development.
        self.send_header('Access-Control-Allow-Origin', settings.ALLOWED_HOSTS)
        self.end_headers()

    def do_GET(self):
        "Handle all get requests."
        resolved_route = router.get_view(self.path, settings.GET_REQUEST)
        view_instance = resolved_route["view"](self)
        self._set_headers(view_instance.headers)
        if resolved_route["route"]:
            self.send_response(200, message="Success")
        else:
            self.send_response(404, message="Not found")
        self.wfile.write(view_instance.render())


def run_server():
    port = settings.PORT
    if not port:
        raise Exception("Set the PORT number in app/settings.py")
    os.chdir(settings.ROOT)
    server_address = ('', port)
    httpd = HTTPServer(server_address, _RequestHandler)
    print('serving at %s:%d' % server_address)
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
