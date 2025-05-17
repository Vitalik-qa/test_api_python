import pytest
import json
import pytest
import requests
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps


# Тест обновление питомца через Форму
def test_post_pet_updates():
    # Создаем JSON
    request = generate_json_steps.create_json_pet_required_params()
    # Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
    # Анализируем ответ
    print("result pretty =", response_post.json())
    assert_steps.assert_not_none_id(response_post)
    # Создаем JSON
    parems = {'name': 'Doggii', 'status': 'available'}
    # Отправлям запрос
    response_post_updates = requests.post(urls.url_pet_get_id(str(response_post.json()['id'])), parems)
    print(response_post_updates.json())
    # Проверяем через GET, что объект изменен
    response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
    print(response_get.json())
    assert_steps.assert_equals_response_ids(response_post, response_get)
    assert_steps.assert_equals_response_names(response_post, response_get)


# Тест обновление питомца через Форму по несуществующему ID
def test_post_pet_updates_id_negative():
    # Создаем JSON
    parems = {'name': 'Doggii', 'status': 'available'}
    # Отправлям запрос
    response_post_updates = requests.post(urls.url_pet_get_id("7777777667777"), parems)
    # Анализируем ответ
    print(response_post_updates.json())
    assert_steps.assert_status_code_404(response_post_updates)
    assert_steps.assert_type_unknown(response_post_updates)


