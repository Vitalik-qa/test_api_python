import pytest
import json
import pytest
import requests
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps



# Тест редактирования  питомца
def test_put_pet():
    # Создаем JSON
    request = generate_json_steps.create_json_pet_required_params()
    # Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
    print("result pretty =", response_post.json())
    # Создаем JSON
    request_put = {}
    request_put['id'] = str(response_post.json()['id'])
    request_put['name'] = support_steps.generate_random_letter_string(8)
    # Отправлям запрос
    response_put = requests.put(urls.url_pet_post, json=request_put)
    print(response_put.json())
    # Проверяем через GET, что объект изменен
    response_get = requests.get(urls.url_pet_get_id(str(response_put.json()['id'])))
    assert_steps.assert_equals_response_names(response_put, response_get)


# Тест редактирования питомца по несуществующему ID
def test_put_pet_id_negative():
    # Создаем JSON
    request = {}
    request['id'] = "name"
    request['name'] = support_steps.generate_random_letter_string(7)
    # Отправлям запрос
    response_put = requests.post(urls.url_pet_post, json=request)
    # Анализируем ответ
    print("result pretty =", response_put.json())
    assert_steps.assert_type_unknown(response_put)


