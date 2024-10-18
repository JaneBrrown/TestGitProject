import httpx
from jsonschema import validate
from core.contracts import UPDATED_USER_SCHEME
import datetime
import allure

BASE_URL = "https://reqres.in/"
UPDATE_USER = "api/users/2"

@allure.suite('Проверка запросов на обновление пользователя методом PUT')
@allure.title('Проверяем обновления данных пользователя методом PUT')
def test_update_user_job_put_with_name_and_job():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + UPDATE_USER}'):
        body = {
        "name": "morpheus",
        "job": "zion resident"
        }
        response = httpx.put(BASE_URL + UPDATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    response_json = response.json()
    date_of_update = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATED_USER_SCHEME)
    with allure.step("Проверяем соответствие имени в запросе/ответе"):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем соответствие работы в запросе/ответе'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем соответствие даты обновления пользователя с текущей датой'):
        assert date_of_update[0:16] == current_date[0:16]


def test_update_user_job_put_without_name():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + UPDATE_USER}'):
        body = {
        "job": "zion resident"
        }
        response = httpx.put(BASE_URL + UPDATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    response_json = response.json()
    date_of_update = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATED_USER_SCHEME)
    with allure.step('Проверяем соответствие работы в запросе/ответе'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем соответствие даты обновления пользователя с текущей датой'):
        assert date_of_update[0:16] == current_date[0:16]


def test_update_user_job_put_without_job():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + UPDATE_USER}'):
        body = {
        "name": "morpheus"
        }
        response = httpx.put(BASE_URL + UPDATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    response_json = response.json()
    date_of_update = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATED_USER_SCHEME)
    with allure.step("Проверяем соответствие имени в запросе/ответе"):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем соответствие даты обновления пользователя с текущей датой'):
        assert date_of_update[0:16] == current_date[0:16]


@allure.suite('Проверка запросов на обновление пользователя методом PATCH')
@allure.title('Проверяем обновления данных пользователя методом PATCH')
def test_update_user_patch_with_name_and_job():
    with allure.step(f'Делаем запрос по адресу:{BASE_URL + UPDATE_USER}'):
        body = {
        "name": "morpehus",
        "job": "zion resident"
        }
        response = httpx.patch(BASE_URL + UPDATE_USER, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    response_json = response.json()
    date_of_update = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, UPDATED_USER_SCHEME)
    with allure.step("Проверяем соответствие имени в запросе/ответе"):
        assert response_json['name'] == body['name']
    with allure.step("Проверяем соответствие работы в запросе/ответе"):
        assert response_json['job'] == body['job']
    with allure.step("Проверяем соответствие даты обновления пользователя с текущей датой"):
        assert date_of_update[0:16] == current_date[0:16]


