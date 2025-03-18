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
    print(request)
    print("result pretty =", response_post.json())

    request_put = {}
    request_put['id'] = str(response_post.json()['id'])
    request_put['name'] = "sberCats"
    print()
    print(request_put)
    response_put = requests.put(url, json=request_put)
    print(response_put.json())
