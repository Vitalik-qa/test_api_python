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
# Тест обновление питомца через Форму
def test_post_pet_updates():
    with allure.step("Создаем JSON"):
        request = generate_json_steps.create_json_pet_required_params()
    with allure.step("Отправлям запрос POST"):
        response_post = requests.post(urls.url_pet_post, json=request)
    with allure.step("Анализируем ответ"):
        print("result pretty =", response_post.json())
        assert_steps.assert_not_none_id(response_post)
    with allure.step("Создаем JSON"):
        parems = {'name': 'Doggii', 'status': 'available'}
    with allure.step("Отправлям запрос POST"):
        response_post_updates = requests.post(urls.url_pet_get_id(str(response_post.json()['id'])), parems)
        print(response_post_updates.json())
    with allure.step("Проверяем через GET, что объект изменен"):
        response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
        print(response_get.json())
        assert_steps.assert_equals_response_ids(response_post, response_get)
        assert_steps.assert_equals_response_names(response_post, response_get)

@pytest.mark.regress_tests
@pytest.mark.negative_tests
# Тест обновление питомца через Форму по несуществующему ID
def test_post_pet_updates_id_negative():
    with allure.step("Создаем JSON"):
        parems = {'name': 'Doggii', 'status': 'available'}
    with allure.step("Отправлям запрос POST"):
         response_post_updates = requests.post(urls.url_pet_get_id("7777777667777"), parems)
    with allure.step("Анализируем ответ"):
        print(response_post_updates.json())
        assert_steps.assert_status_code_404(response_post_updates)
        assert_steps.assert_type_unknown(response_post_updates)


