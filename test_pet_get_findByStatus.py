import pytest
import json
import pytest
import requests
import allure
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps

@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.positive_tests
# Тест поиска питомца по статусу
def test_get_pet_findByStatus():
    with allure.step("Создаем JSON"):
        params = {'status': 'pending'}
    with allure.step("Отправлям запрос GET"):
        response_get = requests.get(urls.url_findByStatus, params=params)
    with allure.step("Анализируем ответ"):
        print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
        assert_steps.assert_status_code_200(response_get)

@pytest.mark.regress_tests
@pytest.mark.negative_tests
# Тест поиска питомца по несуществующему статусу
def test_get_pet_findByStatus_status_negative():
    with allure.step("Создаем JSON"):
        params = {'status': 'dog'}
    with allure.step("Отправлям запрос GET"):
        response_get = requests.get(urls.url_findByStatus, params=params)
    with allure.step("Анализируем ответ"):
        print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
        assert_steps.assert_response_none(response_get)
