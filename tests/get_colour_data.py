import httpx
from jsonschema import validate
from core.contracts import COLOUR_DATA_SCHEME
import allure

BASE_URL = "https://reqres.in/"
LIST_COLOURS = "api/unknown"
SINGLE_COLOUR = "api/unknown/2"
NOT_FOUND_COLOUR = "api/unknown/23"
COLOUR_START= "#"

@allure.suite('Проверка запросов данных цветов')
@allure.title('Проверяем получение списка цветов')
def test_list_colours():
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + LIST_COLOURS}'):
        response = httpx.get(BASE_URL + LIST_COLOURS)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step(f'Проверяем элемент из списка'):
            validate(item, COLOUR_DATA_SCHEME)
            with allure.step('Проверяем, что номер цвета начинается с #'):
                assert item["color"].startswith(COLOUR_START)


@allure.suite('Проверка запросов данных одного цвета')
@allure.title('Проверяем получение данных о цвете')
def test_single_colour():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + SINGLE_COLOUR}'):
        response = httpx.get(BASE_URL + SINGLE_COLOUR)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']

    with allure.step('Проверяем, что номер цвета начинается с #'):
        assert data["color"].startswith(COLOUR_START)

@allure.suite('Проверка отображения страницы не найденного цвета')
@allure.title('Проверка отображения статус кода 404 colour_not_found')
def test_colour_not_found():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + NOT_FOUND_COLOUR}'):
        response = httpx.get(BASE_URL + NOT_FOUND_COLOUR)
    with allure.step('Проверяем отображение статус кода 404'):
        assert response.status_code == 404




