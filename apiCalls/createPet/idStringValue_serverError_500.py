import requests

endpoint = "https://petstore.swagger.io/v2"


# Create a new pet
def test_create_pet():
    payload = {
        "id": "test",
        "category": {"id": 0, "name": "string"},
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available"}
    create_pet_response = requests.post(endpoint + "/pet", json=payload)
    data = create_pet_response.json()
    status = create_pet_response.status_code
    print(data)
    print(status)
    assert create_pet_response.status_code == 500
    pass
