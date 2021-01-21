from funny_endpoints import __version__
from funny_endpoints import Funny
import pytest
from .requester_mock import RequesterMock

def test_version():
    assert __version__ == '0.1.0'

requester = RequesterMock()
funny = Funny(requester)

@pytest.mark.parametrize("method,response,want", [
    (funny.advice, {"slip": { "id": 183, "advice": "Always get two ciders."}}, "Always get two ciders."),
    (funny.chucknorris, {"categories":[],"created_at":"2020-01-05 13:42:24.696555","icon_url":"https://assets.chucknorris.host/img/avatar/chuck-norris.png","id":"3Odt13-SQ06Pq-RUPwRQ4w","updated_at":"2020-01-05 13:42:24.696555","url":"https://api.chucknorris.io/jokes/3Odt13-SQ06Pq-RUPwRQ4w","value":"Peace disturbs Chuck Norris."}, "Peace disturbs Chuck Norris."),
    (funny.dadjoke, {"id":"0DQKB51oGlb","joke":"What did one nut say as he chased another nut?  I'm a cashew!","status":200}, "What did one nut say as he chased another nut?  I'm a cashew!"),
])
def test_funny_api_methods(method, response, want):
    requester.set_response(response)
    got = method()["message"]
    assert got == want

@pytest.mark.parametrize("name,index,response,want", [
    ("Advice", 0, {"slip": { "id": 183, "advice": "Always get two ciders."}}, "Always get two ciders."),
    ("Chuck Norris Joke", 1, {"categories":[],"created_at":"2020-01-05 13:42:24.696555","icon_url":"https://assets.chucknorris.host/img/avatar/chuck-norris.png","id":"3Odt13-SQ06Pq-RUPwRQ4w","updated_at":"2020-01-05 13:42:24.696555","url":"https://api.chucknorris.io/jokes/3Odt13-SQ06Pq-RUPwRQ4w","value":"Peace disturbs Chuck Norris."}, "Peace disturbs Chuck Norris."),
    ("Dad Joke", 2, {"id":"0DQKB51oGlb","joke":"What did one nut say as he chased another nut?  I'm a cashew!","status":200}, "What did one nut say as he chased another nut?  I'm a cashew!"),
])
def test_funny_get_message_index(name, index, response, want):
    requester.set_response(response)
    got = funny.getmessage(index)["message"]
    assert got == name + ": " + want
