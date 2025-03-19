import pytest
import json
import pytest
import requests


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
