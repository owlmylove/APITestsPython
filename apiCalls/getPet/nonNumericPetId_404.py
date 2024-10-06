import requests

endpoint = "https://petstore.swagger.io/v2"


# Read pet by ped_id
def test_get_pet_by_id():
    read_pet_response = requests.get(endpoint + "/pet/test")
    data = read_pet_response.json()
    status_code = read_pet_response.status_code
    print(read_pet_response, data, status_code)
    assert read_pet_response.status_code == 404
    pass
