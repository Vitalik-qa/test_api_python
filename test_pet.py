import pytest
import json
import pytest
import requests

#5
def test_get_pet():
    url = "https://petstore.swagger.io/v2/pet/9223372036854775329"

    response_get = requests.get(url)
    print()
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert response_get.json()['id'] == 9223372036854775329

def test_get_pet_id_negative():
    url = "https://petstore.swagger.io/v2/pet/111111111111"

    response_get = requests.get(url)
    print()
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
    assert response_get.json()['message'] == "Pet not found"

#2
def test_post_pet():
    url = "https://petstore.swagger.io/v2/pet"

    request = {}
    request['name'] = "sberCat"
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(url, json=request)
    print()
    print("result pretty =", response_post.json())
    assert response_post.json()['id'] is not None

    urlGet = "https://petstore.swagger.io/v2/pet/" + str(response_post.json()['id'])
    response_get = requests.get(urlGet)
    print('urlGet', urlGet)
    assert response_get.json()['id'] == response_post.json()['id']

def test_post_pet_name_negative():
    url = "https://petstore.swagger.io/v2/pet"

    request = {}
    request['name'] = "sberCat"
    request['category'] = {}
    request['category']['name'] = []
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(url, json=request)
    print()
    print("result pretty =", response_post.json())
    assert response_post.json()['message'] == "something bad happened"

#3
def test_put_pet():
    url = "https://petstore.swagger.io/v2/pet"

    request = {}
    request['name'] = "sberCat"
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(url, json=request)
    print()
    print("result pretty =", response_post.json())

    request_put = {}
    request_put['id'] = str(response_post.json()['id'])
    request_put['name'] = "sberCats"
    response_put = requests.put(url, json=request_put)
    print()
    print(response_put.json())
    assert response_put.json()['photoUrls'] == []

    urlGet = "https://petstore.swagger.io/v2/pet/" + str(response_put.json()['id'])
    response_get = requests.get(urlGet)
    print('urlGet', urlGet)
    assert response_get.json()['photoUrls'] == []

def test_put_pet_id_negative():
    url = "https://petstore.swagger.io/v2/pet"

    request = {}
    request['id'] = "name"
    request['name'] = "sberCat"
    response_put = requests.post(url, json=request)
    print()
    print("result pretty =", response_put.json())
    assert response_put.json()['message'] == "something bad happened"

#7
def test_delete_pet():
    url = "https://petstore.swagger.io/v2/pet"

    request = {}
    request['name'] = "sberCat"
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(url, json=request)
    print()
    print("result pretty =", response_post.json())

    url_delete = "https://petstore.swagger.io/v2/pet/" + str(response_post.json()['id'])
    response_delete = requests.delete(url_delete)
    print(response_delete)
    assert response_delete.json()['code'] == 200

    urlGet = "https://petstore.swagger.io/v2/pet/" + str(response_post.json()['id'])
    response_get = requests.get(urlGet)
    print('urlGet', response_get.json())
    assert response_get.json()['message'] == "Pet not found"

def test_delete_pet():
    url_delete = "https://petstore.swagger.io/v2/pet/" + "7777777777"
    response_delete = requests.delete(url_delete)
    print(response_delete)
    assert response_delete.status_code == 404

#1
def test_post_pet_uploadImage():
    url = "https://petstore.swagger.io/v2/pet"

    request = {}
    request['name'] = "sberCat"
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(url, json=request)
    print()
    print("result pretty =", response_post.json())
    assert response_post.json()['id'] is not None

    url_uploadImage = "https://petstore.swagger.io/v2/pet/" + str(response_post.json()['id']) +"/uploadImage"
    additional_metadata = {'additionalMetadata': '111'}
    files = {'file': open('test.jpg', 'rb')}
    response_post_uploadImage = requests.post(url_uploadImage, data=additional_metadata, files=files)
    print('url_uploadImage', url_uploadImage)
    print('response_post_uploadImage', response_post_uploadImage.json())
    assert response_post_uploadImage.json()['code'] == 200

def test_post_pet_uploadImage_name_negative():
    url = "https://petstore.swagger.io/v2/pet"

    request = {}
    request['name'] = "sberCat"
    request['category'] = {}
    request['category']['name'] = "cats"
    request['photoUrls'] = ["photoSberCat1"]
    response_post = requests.post(url, json=request)
    print()
    print("result pretty =", response_post.json())
    assert response_post.json()['id'] is not None

    url_uploadImage = "https://petstore.swagger.io/v2/pet/" + "9223372036854776000" +"/uploadImage"
    additional_metadata = {'additionalMetadata': '111'}
    files = {'file': open('test.jpg', 'rb')}
    response_post_uploadImage = requests.post(url_uploadImage, data=additional_metadata, files=files)
    print('url_uploadImage', url_uploadImage)
    print('response_post_uploadImage', response_post_uploadImage.json())
    assert response_post_uploadImage.json()['code'] == 404

# 4 6