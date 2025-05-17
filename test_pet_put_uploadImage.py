import pytest
import json
import pytest
import requests
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps



# Тест загрузки изображения
def test_post_pet_uploadImage():
    # Создаем JSON
    request = generate_json_steps.create_json_pet_required_params()
    # Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
    # Анализируем ответ
    print("result pretty =", response_post.json())
    assert_steps.assert_not_none_id(response_post)
    # Создаем файл
    additional_metadata = {'additionalMetadata': '111'}
    files = {'file': open('test.jpg', 'rb')}
    # Отправлям запрос
    response_post_uploadImage = requests.post(urls.url_uploadImage(str(response_post.json()['id'])),
                                              data=additional_metadata, files=files)
    # Анализируем ответ
    print('response_post_uploadImage', response_post_uploadImage.json())
    assert_steps.assert_status_code_200(response_post_uploadImage)


# Тест загрузки изображения по негативному Name
def test_post_pet_uploadImage_name_negative():
    # Создаем JSON
    request = generate_json_steps.create_json_pet_not_name_params()
    # Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
    # Анализируем ответ
    print("result pretty =", response_post.json())
    assert_steps.assert_not_none_id(response_post)
    # Создаем файл
    additional_metadata = {'additionalMetadata': '111'}
    files = {'file': open('test.jpg', 'rb')}
    # Отправлям запрос
    response_post_uploadImage = requests.post(urls.url_uploadImage("9223372036854776000"), data=additional_metadata,
                                              files=files)
    # Анализируем ответ
    print('response_post_uploadImage', response_post_uploadImage.json())
    assert_steps.assert_status_code_404(response_post_uploadImage)



