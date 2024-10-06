import requests

endpoint = "https://petstore.swagger.io/v2"


# Create a new pet
def test_create_pet():
    payload = {
        "id": 1114587938759308999222222222,
        "category": {"id": 1114587930899, "name": "string"},
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": [{"id": 1114587938752, "name": "string"}],
        "status": "available"}
    create_pet_response = requests.post(endpoint + "/pet", json=payload)
    data = create_pet_response.json()
    status = create_pet_response.status_code
    print(data)
    print(status)
    assert create_pet_response.status_code == 500
    pass

# all id values have the same behaviour as have the same data type
# "id", "category": "id", "tags": "id"
