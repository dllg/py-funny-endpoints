from funny_endpoints import router
from .requester_mock import RequesterMock
import pytest
import json

requester = RequesterMock()
app = router.SetupRoute(requester)
app.testing = True
client = app.test_client()

@pytest.mark.parametrize("url,response,want", [
    ("/v1/advice", {"slip": { "id": 183, "advice": "Always get two ciders."}}, "Always get two ciders."),
    ("/v1/chucknorris", {"categories":[],"created_at":"2020-01-05 13:42:24.696555","icon_url":"https://assets.chucknorris.host/img/avatar/chuck-norris.png","id":"3Odt13-SQ06Pq-RUPwRQ4w","updated_at":"2020-01-05 13:42:24.696555","url":"https://api.chucknorris.io/jokes/3Odt13-SQ06Pq-RUPwRQ4w","value":"Peace disturbs Chuck Norris."}, "Peace disturbs Chuck Norris."),
    ("/v1/dadjoke", {"id":"0DQKB51oGlb","joke":"What did one nut say as he chased another nut?  I'm a cashew!","status":200}, "What did one nut say as he chased another nut?  I'm a cashew!"),
])
def test_endpoints(url, response, want):
    requester.set_response(response)
    r = client.get(url)
    data = json.loads(r.get_data())
    assert 'message' in data
    assert data['message'] == want

def test_random_endpoint():
    requester.set_response(
        {
            "slip": {"advice": "random endpoint result"},
            "value": "random endpoint result",
            "joke": "random endpoint result",
        }
    )
    r = client.get("/v1/random")
    data = json.loads(r.get_data())
    assert 'message' in data
    assert ": random endpoint result" in data["message"]

@pytest.mark.parametrize("url", [
    ("/v1/badadvice"),
    ("/some/strange/endpoint"),
    ("/v2/advice"),
    (""),
])
def test_bad_endpoints(url):
    requester.set_response("")
    r = client.get(url)
    assert '404 NOT FOUND' in "{}".format(r)
