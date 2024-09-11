import httpx
from jsonschema import validate

from core.contracts import COLOUR_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_COLOURS = "api/unknown"
SINGLE_COLOUR = "api/unknown/2"
NOT_FOUND_COLOUR = "api/unknown/23"
COLOUR_START= "#"

def test_list_colours():
    response = httpx.get(BASE_URL + LIST_COLOURS)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, COLOUR_DATA_SCHEME)
        assert item["color"].startswith(COLOUR_START)

def test_single_colour():
    response = httpx.get(BASE_URL + SINGLE_COLOUR)
    assert response.status_code == 200
    data = response.json()['data']
    assert data["color"].startswith(COLOUR_START)

def test_colour_not_found():
    response = httpx.get(BASE_URL + NOT_FOUND_COLOUR)
    assert response.status_code == 404




