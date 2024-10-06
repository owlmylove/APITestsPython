import requests

endpoint = "https://petstore.swagger.io/v2"


# Create a new pet
def test_create_pet():
    payload = {
        "id": 2,
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
def test_get_pet_by_id():
    read_pet_response = requests.get(endpoint + "/pet/2")
    data = read_pet_response.json()
    status_code = read_pet_response.status_code
    print(read_pet_response, data, status_code)
    assert read_pet_response.status_code == 200
    pass


# Update pet
def test_update_pet():
    payload = {
        "id": 2,
        "category": {"id": 0, "name": "dog"},
        "name": "Almond",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available"}
    update_pet_response = requests.put(endpoint + "/pet", json=payload)
    data = update_pet_response.json()
    status_code = update_pet_response.status_code
    assert update_pet_response.status_code == 200
    print(update_pet_response, data, status_code)
    pass


def test_delete_pet():
    delete_pet_response = requests.delete(endpoint + "/pet/2")
    data = delete_pet_response.json()
    status_code = delete_pet_response.status_code
    assert delete_pet_response.status_code == 200
    print(delete_pet_response, data, status_code)
    pass
