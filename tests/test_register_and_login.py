import json
import httpx
import pytest
from jsonschema import validate
from core.contracts import REGISTER_USER_SCHEME
import allure
from core.contracts import LOGIN_USER_SCHEME

BASE_URL = "https://reqres.in/"
REGISTER_USER = "api/register"

json_file = open('core/new_users_data.json')
users_data = json.load(json_file)


@allure.suite('Проверка запросов на регистрацию пользователя')
@allure.title('Регистрируем нового пользователя')
@pytest.mark.parametrize('users_data', users_data)
def test_register_success(users_data):
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + REGISTER_USER}'):
        response = httpx.post(BASE_URL + REGISTER_USER, json = users_data)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    validate(response.json(), REGISTER_USER_SCHEME)


@allure.title('Проверка запроса на регистрацию без пароля')
def test_register_unsuccessful():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + REGISTER_USER}'):

        body = {
            "email": "sydney@fife"
        }
    response = httpx.post(BASE_URL + REGISTER_USER, json = body)
    with allure.step ('Проверяем код ответа'):
        assert response.status_code == 400


BASE_URL = "https://reqres.in/"
LOGIN_URL = "api/login"

json_file = open ('core/users_login_data.json')
login_data = json.load(json_file)

@pytest.mark.parametrize('login_data', login_data)
@allure.title('Проверка логина пользователя')
def test_login_success(login_data):
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + LOGIN_URL}'):
        response = httpx.post(BASE_URL + LOGIN_URL, json = login_data)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    validate(response.json(), LOGIN_USER_SCHEME)
