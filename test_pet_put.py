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
# Тест редактирования  питомца
def test_put_pet():
    with allure.step("Создаем JSON"):
        request = generate_json_steps.create_json_pet_required_params()
    with allure.step("Отправлям запрос POST"):
        response_post = requests.post(urls.url_pet_post, json=request)
        print("result pretty =", response_post.json())
    with allure.step("Создаем JSON"):
        request_put = {}
        request_put['id'] = str(response_post.json()['id'])
        request_put['name'] = support_steps.generate_random_letter_string(8)
    with allure.step("Отправлям запрос PUT"):
        response_put = requests.put(urls.url_pet_post, json=request_put)
        print(response_put.json())
    with allure.step("Проверяем через GET, что объект изменен"):
        response_get = requests.get(urls.url_pet_get_id(str(response_put.json()['id'])))
        assert_steps.assert_equals_response_names(response_put, response_get)

@pytest.mark.regress_tests
@pytest.mark.negative_tests
# Тест редактирования питомца по несуществующему ID
def test_put_pet_id_negative():
    with allure.step("Создаем JSON"):
        request = {}
        request['id'] = "name"
        request['name'] = support_steps.generate_random_letter_string(7)
    with allure.step("Отправлям запрос PUT"):
        response_put = requests.put(urls.url_pet_post, json=request)
    with allure.step("Анализируем ответ"):
        print("result pretty =", response_put.json())
        assert_steps.assert_type_unknown(response_put)


