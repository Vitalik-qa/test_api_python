import pytest
import json
import pytest
import requests
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps


# Тест удаления питомца
def test_delete_pet():
    # Создаем JSON
    request = generate_json_steps.create_json_pet_required_params()
    # Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
    print("result pretty =", response_post.json())
    # Отправлям запрос
    response_delete = requests.delete(urls.url_pet_get_id(str(response_post.json()['id'])))
    # Анализируем ответ
    print(response_delete)
    assert_steps.assert_status_code_200(response_delete)
    # Проверяем через GET, что объект удален
    response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
    print('urlGet', response_get.json())
    assert_steps.assert_type_error(response_get)


# Тест удаление питомца по несуществующему ID
def test_delete_pet_id_negative():
    # Отправлям запрос
    response_delete = requests.delete(urls.url_pet_get_id("777777777"))
    # Анализируем ответ
    print(response_delete)
    assert_steps.assert_status_code_404(response_delete)
