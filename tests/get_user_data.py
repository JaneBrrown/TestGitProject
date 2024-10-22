import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME
import allure

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
SINGLE_USER = "api/users/2"
USER_NOT_FOUND = "api/users/23"
EMAIL_ENDS = "@reqres.in"
AVATAR_ENDS = "-image.jpg"

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение списка пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + LIST_USERS}'):
        response = httpx.get(BASE_URL + LIST_USERS)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step(f'Проверяем элемент из списка'):
            validate(item, USER_DATA_SCHEME)
            with allure.step('Проверяем окончание имэйл адреса'):
                assert item['email'].endswith(EMAIL_ENDS)
            with allure.step('Проверяем наличие айди в ссылке на аватарку'):
                assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)

@allure.suite('Проверка запросов данных одного пользователя')
@allure.title('Проверяем получение данных пользователя')
def test_single_user():
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + SINGLE_USER}'):
        response = httpx.get(BASE_URL + SINGLE_USER)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']

    with allure.step('Проверяем окончание имэйл адреса'):
        assert data['email'].endswith(EMAIL_ENDS)
    with allure.step('Проверяем наличие айди в ссылке на аватарку'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

@allure.suite('Проверка отображения страницы не найденного пользователя')
@allure.title('Проверка отображения статус кода 404 user_not_found')
def test_user_not_found():
    response = httpx.get(BASE_URL + USER_NOT_FOUND)
    with allure.step('Проверяем отображение статус кода 404'):
        assert response.status_code == 404

