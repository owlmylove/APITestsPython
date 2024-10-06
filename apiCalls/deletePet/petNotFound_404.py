import requests

endpoint = "https://petstore.swagger.io/v2"


# Create a new pet
def test_create_pet():
    payload = {
        "id": 5,
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


# Remove just created pet
def test_delete_pet():
    delete_pet_response = requests.delete(endpoint + "/pet/5")
    data = delete_pet_response.json()
    status_code = delete_pet_response.status_code
    assert delete_pet_response.status_code == 200
    print(delete_pet_response, data, status_code)
    pass


# Try to delete removed pet again
def test_delete_pet_not_found():
    delete_pet_response = requests.delete(endpoint + "/pet/5")
    status_code = delete_pet_response.status_code
    assert delete_pet_response.status_code == 404
    print(status_code)
    pass
