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
