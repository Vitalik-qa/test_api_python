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
    print(url_delete)

    response_delete = requests.delete(url_delete)
    print(response_delete)


