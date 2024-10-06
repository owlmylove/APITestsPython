import requests

endpoint = "https://petstore.swagger.io/v2"


# Create a new pet
def test_create_pet():
    payload = {
        "id": 1,
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


def test_delete_pet():
    delete_pet_response = requests.delete(endpoint + "/pet/1")
    data = delete_pet_response.json()
    status_code = delete_pet_response.status_code
    assert delete_pet_response.status_code == 200
    print(delete_pet_response, data, status_code)
    pass
