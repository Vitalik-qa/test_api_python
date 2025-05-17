import pytest
import json
import pytest
import requests
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps


# Тест поиска питомца по статусу
def test_get_pet_findByStatus():
    # Создаем JSON
    params = {'status': 'pending'}
    # Отправлям запрос
    response_get = requests.get(urls.url_findByStatus, params=params)
    # Анализируем ответ
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert_steps.assert_status_code_200(response_get)


# Тест поиска питомца по несуществующему статусу
def test_get_pet_findByStatus_status_negative():
    # Создаем JSON
    params = {'status': 'dog'}
    # Отправлям запрос
    response_get = requests.get(urls.url_findByStatus, params=params)
    # Анализируем ответ
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert_steps.assert_response_none(response_get)
