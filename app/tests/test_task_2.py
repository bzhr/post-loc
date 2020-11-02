import pytest
import json

from ..views import StoresApiView
from ..router import Router
from ..settings import GET_REQUEST


class MockRequest:

    def __init__(self, path):
        self.path = path


@pytest.fixture(scope="module")
def router():
    return Router()


def test_resolve_route(router):
    request = MockRequest(path="/api/stores?q=rh")
    resolved_route = router.get_view(request.path, GET_REQUEST)
    assert resolved_route["route"]
    view = resolved_route.get("view")
    assert view
    view_instance = view(request)
    assert isinstance(view_instance, StoresApiView)


def test_response(router):
    request = MockRequest(path="/api/stores?q=rh")
    resolved_route = router.get_view(request.path, GET_REQUEST)
    view = resolved_route.get("view")
    view_instance = view(request)
    response = json.loads(view_instance.render())
    assert type(response) == list
    assert len(response) > 0
    assert response[0]["name"]
    assert response[0]["postcode"]


def test_query(router):
    request = MockRequest(path="/api/stores?q=br")
    resolved_route = router.get_view(request.path, GET_REQUEST)
    view = resolved_route.get("view")
    view_instance = view(request)
    response = json.loads(view_instance.render())
    assert response[0]["postcode"] == "BR5 3RP"
    assert response[1]["name"] == "Bracknell"
