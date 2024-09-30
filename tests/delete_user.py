import httpx
from jsonschema import validate
import allure


BASE_URL = "https://reqres.in/"
DELETE_USER = "api/users/2"

@allure.suite('Проверка запросов на удаление пользователя')
@allure.title('Проверяем удаление пользователя')
def test_user_deletion():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + DELETE_USER}'):
        response = httpx.delete(BASE_URL + DELETE_USER)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 204

