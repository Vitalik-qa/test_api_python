import pytest
import json
import pytest
import requests


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


