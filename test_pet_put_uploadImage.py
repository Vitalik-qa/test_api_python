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
# Тест загрузки изображения
def test_post_pet_uploadImage():
    with allure.step("Создаем JSON"):
        request = generate_json_steps.create_json_pet_required_params()
    with allure.step("Отправлям запрос POST"):
        response_post = requests.post(urls.url_pet_post, json=request)
    with allure.step("Анализируем ответ"):
        print("result pretty =", response_post.json())
        assert_steps.assert_not_none_id(response_post)
    with allure.step("Создаем файл"):
        additional_metadata = {'additionalMetadata': '111'}
        files = {'file': open('test.jpg', 'rb')}
    with allure.step("Отправлям запрос POST"):
        response_post_uploadImage = requests.post(urls.url_uploadImage(str(response_post.json()['id'])),
                                              data=additional_metadata, files=files)
    with allure.step("Анализируем ответ"):
        print('response_post_uploadImage', response_post_uploadImage.json())
        assert_steps.assert_status_code_200(response_post_uploadImage)

@pytest.mark.regress_tests
@pytest.mark.negative_tests
# Тест загрузки изображения по негативному Name
def test_post_pet_uploadImage_name_negative():
    with allure.step("Создаем JSON"):
        request = generate_json_steps.create_json_pet_not_name_params()
    with allure.step("Отправлям запрос POST"):
        response_post = requests.post(urls.url_pet_post, json=request)
    with allure.step("Анализируем ответ"):
        print("result pretty =", response_post.json())
        assert_steps.assert_not_none_id(response_post)
    # Создаем файл
    additional_metadata = {'additionalMetadata': '111'}
    files = {'file': open('test.jpg', 'rb')}
    with allure.step("Отправлям запрос POST"):
        response_post_uploadImage = requests.post(urls.url_uploadImage("9223372036854776000"), data=additional_metadata,
                                              files=files)
    with allure.step("Анализируем ответ"):
        print('response_post_uploadImage', response_post_uploadImage.json())
        assert_steps.assert_status_code_404(response_post_uploadImage)



