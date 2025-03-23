import pytest
import json
import pytest
import requests

#User для методов: POST / user, PUT / user / {username}, GET / user / {username}, DELETE / user / {username}.


def test_put_pet():
    url = "https://petstore.swagger.io/v2/pet"

    request = {}
    request['id'] = 1111
    request['petId'] = 1
    request['quantity'] = 11
    request['shipDate'] = "2025-03-21T19:23:35.187Z"
    request['status'] = "placed"
    request['complete'] = True

    #response_post = requests.post(url, json=request)
    print()
    print("result pretty =", request)



