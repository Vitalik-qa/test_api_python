# Функцмя проверяет утверждение, что  status 200
def assert_status_code_200(response):
    print(response)
    assert response.status_code == 200
    print("PASSED")

# Функцмя проверяет утверждение, что  status 404
def assert_status_code_404(response):
    print(response)
    assert response.status_code == 404
    print("PASSED")


# Функцмя проверяет утверждение, что  id не пустой
def assert_not_none_id(response):
    print(response)
    assert response.json()['id'] is not None
    print("PASSED")


# Функцмя проверяет утверждение, что  id  в запросах равны
def assert_equals_response_ids(first, second):
    print("first =", first.json())
    print("second =", second.json())
    assert first.json()['id'] == second.json()['id']
    print("PASSED")


# Функцмя проверяет утверждение, что  name  в запросах равны
def assert_equals_response_names(first, second):
    print("first =", first.json())
    print("second =", second.json())
    assert first.json()['name'] == second.json()['name']
    print("PASSED")


# Функцмя проверяет утверждение, что  type равен error
def assert_type_error(response):
    print(response)
    assert response.json()['type'] == "error"
    print("PASSED")


# Функцмя проверяет утверждение, что  type равен unknown
def assert_type_unknown(response):
    print(response)
    assert response.json()['type'] == "unknown"
    print("PASSED")

# Функцмя проверяет утверждение, что  ответ пустой
def assert_response_none(response):
    print(response)
    assert response.json() == []
    print("PASSED")