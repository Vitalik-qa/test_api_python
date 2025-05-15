import pytest
import json
import pytest
import requests
import resources.urls as urls
import Steps.support_steps as support_steps


# Тест получения  питомца
def test_get_pet_id():
# Отправляем запрос
    response_get = requests.get(urls.url_pet_get_id("9223372036854775329"))
# Анализируем ответ
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert response_get.json()['id'] == 9223372036854775329

# Тест получения  питомца по несуществующему ID
def test_get_pet_id_negative():
    # Отправляем запрос
    response_get = requests.get(urls.url_pet_get_id("111111111111"))
# Анализируем ответ
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert response_get.json()['message'] == "Pet not found"

# Тест создания нового питомца
def test_post_pet():
# Создаем JSON
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
# Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
# Анализируем ответ
    print("result pretty =", response_post.json())
    assert response_post.json()['id'] is not None
# Проверяем через GET, что объект создан
    response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
    assert response_get.json()['id'] == response_post.json()['id']

# Тест создания нового питомца c негативным Name
def test_post_pet_name_negative():
# Создаем JSON
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['category'] = {}
    request['category']['name'] = []
    request['photoUrls'] = ["photoSberCat1"]
# Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
# Анализируем ответ
    print("result pretty =", response_post.json())
    assert response_post.json()['message'] == "something bad happened"

# Тест редактирования  питомца
def test_put_pet():
# Создаем JSON
    request = {}
    request['name'] = support_steps.generate_random_letter_string(7)
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
# Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
    print("result pretty =", response_post.json())
# Создаем JSON
    request_put = {}
    request_put['id'] = str(response_post.json()['id'])
    request_put['name'] = support_steps.generate_random_letter_string(8)
# Отправлям запрос
    response_put = requests.put(urls.url_pet_post, json=request_put)
# Анализируем ответ
    print(response_put.json())
    assert response_put.json()['photoUrls'] == []
# Проверяем через GET, что объект изменен
    response_get = requests.get(urls.url_pet_get_id(str(response_put.json()['id'])))
    assert response_get.json()['photoUrls'] == []

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
    assert response_put.json()['message'] == "something bad happened"


# Тест удаления питомца
def test_delete_pet():
# Создаем JSON
    request = {}
    request['name'] = support_steps.generate_random_letter_string(5)
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
# Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
    print("result pretty =", response_post.json())
# Отправлям запрос
    response_delete = requests.delete(urls.url_pet_get_id(str(response_post.json()['id'])))
# Анализируем ответ
    print(response_delete)
    assert response_delete.json()['code'] == 200
# Проверяем через GET, что объект удален
    response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
    print('urlGet', response_get.json())
    assert response_get.json()['message'] == "Pet not found"

# Тест удаление питомца по несуществующему ID
def test_delete_pet_id_negative():
# Отправлям запрос
    response_delete = requests.delete(urls.url_pet_get_id("777777777"))
# Анализируем ответ
    print(response_delete)
    assert response_delete.status_code == 404

# Тест загрузки изображения
def test_post_pet_uploadImage():
# Создаем JSON
    request = {}
    request['name'] = "sberCat"
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
# Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
# Анализируем ответ
    print("result pretty =", response_post.json())
    assert response_post.json()['id'] is not None

    additional_metadata = {'additionalMetadata': '111'}
    files = {'file': open('test.jpg', 'rb')}
# Отправлям запрос
    response_post_uploadImage = requests.post(urls.url_uploadImage(str(response_post.json()['id'])),
                                              data=additional_metadata, files=files)
# Анализируем ответ
    print('response_post_uploadImage', response_post_uploadImage.json())
    assert response_post_uploadImage.json()['code'] == 200

# Тест загрузки изображения по негативному Name
def test_post_pet_uploadImage_name_negative():
# Создаем JSON
    request = {}
    request['name'] = "sberCat"
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
# Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
# Анализируем ответ
    print("result pretty =", response_post.json())
    assert response_post.json()['id'] is not None
# Создаем JSON
    additional_metadata = {'additionalMetadata': '111'}
    files = {'file': open('test.jpg', 'rb')}
# Отправлям запрос
    response_post_uploadImage = requests.post(urls.url_uploadImage("9223372036854776000"), data=additional_metadata,
                                              files=files)
# Анализируем ответ
    print('response_post_uploadImage', response_post_uploadImage.json())
    assert response_post_uploadImage.json()['code'] == 404

# Тест поиска питомца по статусу
def test_get_pet_findByStatus():
# Создаем JSON
    params = {'status': 'pending'}
# Отправлям запрос
    response_get = requests.get(urls.url_findByStatus, params=params)
# Анализируем ответ
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert response_get.status_code == 200

# Тест поиска питомца по несуществующему статусу
def test_get_pet_findByStatus_status_negative():
# Создаем JSON
    params = {'status': 'dog'}
# Отправлям запрос
    response_get = requests.get(urls.url_findByStatus, params=params)
# Анализируем ответ
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert response_get.json() == []

# Тест обновление питомца через Форму
def test_post_pet_updates():
# Создаем JSON
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
# Отправлям запрос
    response_post = requests.post(urls.url_pet_post, json=request)
# Анализируем ответ
    print("result pretty =", response_post.json())
    assert response_post.json()['id'] is not None
# Создаем JSON
    parems = {'name': 'Doggii', 'status': 'available'}
# Отправлям запрос
    response_post_updates = requests.post(urls.url_pet_get_id(str(response_post.json()['id'])), parems)
    print(response_post_updates.json())
# Проверяем через GET, что объект изменен
    response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
    print(response_get.json())
    assert response_get.json()['id'] == response_post.json()['id']
    assert response_get.json()['name'] == 'Doggii'
    assert response_get.json()['status'] == 'available'

# Тест обновление питомца через Форму по несуществующему ID
def test_post_pet_updates_id_negative():
# Создаем JSON
    parems = {'name': 'Doggii', 'status': 'available'}
# Отправлям запрос
    response_post_updates = requests.post(urls.url_pet_get_id("7777777667777"), parems)
# Анализируем ответ
    print(response_post_updates.json())
    assert response_post_updates.json()['code'] == 404
    assert response_post_updates.json()['type'] == 'unknown'
    assert response_post_updates.json()['message'] == 'not found'
