import pytest
import json
import pytest
import requests


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
