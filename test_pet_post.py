import pytest
import json
import pytest
import requests
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps



# Тест создания нового питомца
def test_post_pet():
    # Создаем JSON c с обязательными параметрами
    request = generate_json_steps.create_json_pet_required_params()
    # Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
    # Анализируем ответ
    assert_steps.assert_not_none_id(response_post)
    # Проверяем через GET, что объект создан
    response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
    assert_steps.assert_equals_response_ids(response_post, response_get)


# Тест создания нового питомца c негативным Name
def test_post_pet_name_negative():
    # Создаем JSON
    request = generate_json_steps.create_json_pet_not_name_params()
    # Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
    # Анализируем ответ
    print("result pretty =", response_post.json())
    assert_steps.assert_type_unknown(response_post)

