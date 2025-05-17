import pytest
import json
import pytest
import requests
import allure
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps



@allure.step("GET")
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.positive_tests
# Тест создания нового питомца
def test_pet():
    with allure.step("Создаем JSON"):
        request = generate_json_steps.create_json_pet_required_params()
    with allure.step("Отправлям запрос POST"):
        response_post = requests.post(urls.url_pet_post, json=request)
    with allure.step("Анализируем ответ"):
        assert_steps.assert_not_none_id(response_post)
    with allure.step("Отправлям запрос GET, чтобы проверить, что объект создан"):
        response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
        assert_steps.assert_equals_response_ids(response_post, response_get)
        assert_steps.assert_equals_response_names(response_post, response_get)


@allure.step("GET")
@pytest.mark.regress_tests
@pytest.mark.negative_tests
# Тест получения  питомца по несуществующему ID
def test_get_pet_id_negative():
    with allure.step("Отправлям запрос GET"):
        response_get = requests.get(urls.url_pet_get_id("111111111111"))
    with allure.step("Анализируем ответ"):
        print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
        assert_steps.assert_type_error(response_get)
