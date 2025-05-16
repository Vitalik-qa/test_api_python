import Steps.support_steps as support_steps


# Создаем JSON  с обязательными параметрами
def create_json_pet_required_params():
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['category'] = {}
    request['category']['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrts'] = [support_steps.generate_random_letter_string(6)]
    print(request)
    return request


# Создаем JSON  со всеми параметрами
def create_json_pet_all_params():
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['category'] = {}
    request['category']['name'] = support_steps.generate_random_letter_string(6)
    request['photoUris'] = [support_steps.generate_random_letter_string(6)]
    request['tags'] = [{}]
    request['tags'][0]['name'] = support_steps.generate_random_letter_string(6)
    request['status'] = "available"
    print(request)
    return request
