import httpx
from jsonschema import validate
from core.contracts import CREATED_USER_SCHEME
import datetime
import allure

BASE_URL = "https://reqres.in/"
CREATE_USER = "api/users"


@allure.suite('Проверка запросов на создание пользователя')
@allure.title('Проверяем создание нового пользователя')
def test_create_user_with_name_and_job():
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + CREATE_USER}'):
        body = {
            "name": "morpheus",
            "job": "leader"
        }
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201
    response_json = response.json()

    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEME)
    with allure.step('Проверяем соответствие имени в запросе/ответе'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем соответствие работы в запросе/ответе'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем соответствие даты создания пользователя в запросе/ответе'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка запросов на создание пользователя без имени')
@allure.title('Проверяем создание нового пользователя без имени')
def test_create_user_without_name():
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + CREATE_USER}'):
        body = {
            "job": "leader"
        }
    response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEME)
    with allure.step('Проверяем соответствие работы в запросе/ответе'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем соответствие даты создания пользователя в запросе/ответе'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка запросов на создание пользователя без работы')
@allure.title('Проверяем создание нового пользователя без работы')
def test_create_user_without_job():
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + CREATE_USER}'):
        body = {
        "name": "morpheus"
        }
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATED_USER_SCHEME)
    with allure.step('Проверяем соответствие имени в запросе/ответе'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем соответствие даты создания пользователя в запросе/ответе'):
        assert creation_date[0:16] == current_date[0:16]
