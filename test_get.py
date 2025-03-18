import pytest
import json
import pytest
import requests


def test_get_pet():
    url = "https://petstore.swagger.io/v2/pet/1"

    response_get = requests.get(url)
    print()
    print("result pretty =", json.dumps(response_get.json(), indent=4, sort_keys=True))
