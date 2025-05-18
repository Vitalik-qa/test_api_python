import pytest
import json
import pytest
import requests
import allure
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.assert_steps as assert_steps


# Тест получения  питомца по несуществующему ID
def test_get_pet_id_negative():
    # Отправляем запрос
    response_get = requests.get(urls.url_pet_get_id("111111111111"))
    # Анализируем ответ
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert_steps.assert_type_error(response_get)

@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.positive_tests
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

@pytest.mark.regress_tests
@pytest.mark.negative_tests
# Тест создания нового питомца c негативным Name
def test_post_pet_name_negative():
    # Создаем JSON
    request = generate_json_steps.create_json_pet_not_name_params()
    # Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
    # Анализируем ответ
    print("result pretty =", response_post.json())
    assert_steps.assert_type_unknown(response_post)

@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.positive_tests
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

@pytest.mark.regress_tests
@pytest.mark.negative_tests
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

@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.positive_tests
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

@pytest.mark.regress_tests
@pytest.mark.negative_tests
# Тест удаление питомца по несуществующему ID
def test_delete_pet_id_negative():
    # Отправлям запрос
    response_delete = requests.delete(urls.url_pet_get_id("777777777"))
    # Анализируем ответ
    print(response_delete)
    assert_steps.assert_status_code_404(response_delete)

@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.positive_tests
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

@pytest.mark.regress_tests
@pytest.mark.negative_tests
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

@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.positive_tests
# Тест поиска питомца по статусу
def test_get_pet_findByStatus():
    # Создаем JSON
    params = {'status': 'pending'}
    # Отправлям запрос
    response_get = requests.get(urls.url_findByStatus, params=params)
    # Анализируем ответ
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert_steps.assert_status_code_200(response_get)

@pytest.mark.regress_tests
@pytest.mark.negative_tests
# Тест поиска питомца по несуществующему статусу
def test_get_pet_findByStatus_status_negative():
    # Создаем JSON
    params = {'status': 'dog'}
    # Отправлям запрос
    response_get = requests.get(urls.url_findByStatus, params=params)
    # Анализируем ответ
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert_steps.assert_response_none(response_get)

@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.positive_tests
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

@pytest.mark.regress_tests
@pytest.mark.negative_tests
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


