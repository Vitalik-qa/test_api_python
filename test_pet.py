import pytest
import json
import pytest
import requests
import resources.urls as urls
import Steps.support_steps as support_steps

# 5
def test_get_pet_id():

    response_get = requests.get(urls.url_pet_get_id("9223372036854775329"))
    print()
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert response_get.json()['id'] == 9223372036854775329

def test_get_pet_id_negative():

    response_get = requests.get(urls.url_pet_get_id("111111111111"))
    print()
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert response_get.json()['message'] == "Pet not found"

# 2
def test_post_pet():

    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(urls.url_pet_post, json=request)
    print()
    print("result pretty =", response_post.json())
    assert response_post.json()['id'] is not None

    response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
    assert response_get.json()['id'] == response_post.json()['id']


def test_post_pet_name_negative():
    url = "https://petstore.swagger.io/v2/pet"

    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['category'] = {}
    request['category']['name'] = []
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(urls.url_pet_post, json=request)
    print()
    print("result pretty =", response_post.json())
    assert response_post.json()['message'] == "something bad happened"

# 3
def test_put_pet():

    request = {}
    request['name'] = support_steps.generate_random_letter_string(7)
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(urls.url_pet_post, json=request)
    print()
    print("result pretty =", response_post.json())

    request_put = {}
    request_put['id'] = str(response_post.json()['id'])
    request_put['name'] = support_steps.generate_random_letter_string(8)
    response_put = requests.put(urls.url_pet_post, json=request_put)
    print()
    print(response_put.json())
    assert response_put.json()['photoUrls'] == []

    response_get = requests.get(urls.url_pet_get_id(str(response_put.json()['id'])))
    assert response_get.json()['photoUrls'] == []


def test_put_pet_id_negative():

    request = {}
    request['id'] = "name"
    request['name'] = support_steps.generate_random_letter_string(7)
    response_put = requests.post(urls.url_pet_post, json=request)
    print()
    print("result pretty =", response_put.json())
    assert response_put.json()['message'] == "something bad happened"

# 7
def test_delete_pet():

    request = {}
    request['name'] = support_steps.generate_random_letter_string(5)
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(urls.url_pet_post, json=request)
    print()
    print("result pretty =", response_post.json())

    response_delete = requests.delete(urls.url_pet_get_id(str(response_post.json()['id'])))
    print(response_delete)
    assert response_delete.json()['code'] == 200

    response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
    print('urlGet', response_get.json())
    assert response_get.json()['message'] == "Pet not found"


def test_delete_pet_id_negative():

    response_delete = requests.delete(urls.url_pet_get_id("777777777"))
    print(response_delete)
    assert response_delete.status_code == 404

# 1
def test_post_pet_uploadImage():

    request = {}
    request['name'] = "sberCat"
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(urls.url_pet_post, json=request)
    print()
    print("result pretty =", response_post.json())
    assert response_post.json()['id'] is not None

    additional_metadata = {'additionalMetadata': '111'}
    files = {'file': open('test.jpg', 'rb')}
    response_post_uploadImage = requests.post(urls.url_uploadImage(str(response_post.json()['id'])), data=additional_metadata, files=files)
    print('response_post_uploadImage', response_post_uploadImage.json())
    assert response_post_uploadImage.json()['code'] == 200


def test_post_pet_uploadImage_name_negative():
    request = {}
    request['name'] = "sberCat"
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(urls.url_pet_post, json=request)
    print()
    print("result pretty =", response_post.json())
    assert response_post.json()['id'] is not None

    additional_metadata = {'additionalMetadata': '111'}
    files = {'file': open('test.jpg', 'rb')}
    response_post_uploadImage = requests.post(urls.url_uploadImage("9223372036854776000"), data=additional_metadata, files=files)
    print('response_post_uploadImage', response_post_uploadImage.json())
    assert response_post_uploadImage.json()['code'] == 404

# 4
def test_get_pet_findByStatus():

    params = {'status': 'pending'}
    response_get = requests.get(urls.url_findByStatus, params=params)
    print()
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert response_get.status_code == 200

def test_get_pet_findByStatus_status_negative():

    params = {'status': 'dog'}
    response_get = requests.get(urls.url_findByStatus, params=params)
    print()
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert response_get.json() == []

# 6
def test_post_pet_updates():

    request = {}
    request['name'] =  support_steps.generate_random_letter_string(6)
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(urls.url_pet_post, json=request)
    print()
    print("result pretty =", response_post.json())
    assert response_post.json()['id'] is not None

    parems = {'name': 'Doggii', 'status': 'available'}
    response_post_updates = requests.post(urls.url_pet_get_id(str(response_post.json()['id'])), parems)
    print(response_post_updates.json())

    response_get = requests.get(urls.url_pet_get_id(str(response_post.json()['id'])))
    print(response_get.json())
    assert response_get.json()['id'] == response_post.json()['id']
    assert response_get.json()['name'] == 'Doggii'
    assert response_get.json()['status'] == 'available'

def test_post_pet_updates_id_negative():

    parems = {'name': 'Doggii', 'status': 'available'}
    response_post_updates = requests.post(urls.url_pet_get_id("7777777667777"), parems)
    print(response_post_updates.json())

    assert response_post_updates.json()['code'] == 404
    assert response_post_updates.json()['type'] == 'unknown'
    assert response_post_updates.json()['message'] == 'not found'
