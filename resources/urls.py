main_url = "https://petstore.swagger.io/v2/"
url_pet_post = main_url + "pet"
url_findByStatus = "https://petstore.swagger.io/v2/pet/findByStatus"
def url_pet_get_id(pet_id):
    return main_url + "pet/" + pet_id
def url_uploadImage(pet_id):
    return main_url + "pet/" + pet_id + "/uploadImage"

