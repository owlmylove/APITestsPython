import requests

endpoint = "https://petstore.swagger.io/v2"


def test_create_pet():
    payload = {
        "id": 3,
        "category": {"id": 0, "name": "string"},
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": [{"id": 0,"name": "string"}],
        "status": "available"}
    create_pet_response = requests.post(endpoint + "/pet", json=payload)
    data = create_pet_response.json()
    pet_id = data["id"]
    print(f"id: {pet_id}")
    assert create_pet_response.status_code == 200
    pass


# Read pet by ped_id
def test_get_pet_by_id_positive():
    read_pet_response = requests.get(endpoint + "/pet/3")
    data = read_pet_response.json()
    status_code = read_pet_response.status_code
    print(read_pet_response, data, status_code)
    assert read_pet_response.status_code == 200
    pass


def test_get_pet_by_invalid_id():
    read_pet_response = requests.get(endpoint + "/pet/invalid")
    data = read_pet_response.json()
    status_code = read_pet_response.status_code
    print(read_pet_response, data, status_code)
    assert read_pet_response.status_code == 400
    pass



def test_get_pet_not_found():
    read_pet_response = requests.get(endpoint + "/pet/0")
    data = read_pet_response.json()
    status_code = read_pet_response.status_code
    print(read_pet_response, data, status_code)
    assert read_pet_response.status_code == 404
    pass


def test_get_pet_by_empty_id():
    read_pet_response = requests.get(endpoint + "/pet/")
    data = read_pet_response.json()
    status_code = read_pet_response.status_code
    print(read_pet_response, data, status_code)
    assert read_pet_response.status_code == 405
    pass
