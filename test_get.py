import pytest
import json
import pytest
import requests


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
