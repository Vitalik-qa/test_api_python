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
# Тест удаления питомца
def test_delete_pet():
    with allure.step("Создаем JSON"):
        request = generate_json_steps.create_json_pet_required_params()
    with allure.step("Отправлям запрос POST"):
        response_post = requests.post(urls.url_pet_post, json=request)
        print("result pretty =", response_post.json())
    with allure.step("Отправлям запрос DELETE"):
        response_delete = requests.delete(urls.url_pet_get_id(str(response_post.json()['id'])))
    with allure.step("Анализируем ответ"):
        print(response_delete)
        assert_steps.assert_status_code_200(response_delete)
    with allure.step("Проверяем через GET, что объект удален"):
        response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
        print('urlGet', response_get.json())
        assert_steps.assert_type_error(response_get)

@pytest.mark.regress_tests
@pytest.mark.negative_tests
# Тест удаление питомца по несуществующему ID
def test_delete_pet_id_negative():
    with allure.step("Отправлям запрос DELETE"):
        response_delete = requests.delete(urls.url_pet_get_id("777777777"))
    with allure.step("Анализируем ответ"):
        print(response_delete)
        assert_steps.assert_status_code_404(response_delete)
