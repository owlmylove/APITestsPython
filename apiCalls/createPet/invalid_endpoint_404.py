import requests

endpoint = "https://petstore.swagger.io/v2"


# Create a new pet
def test_create_pet():
    payload = {
        "id": "",
        "category": {"id": 0, "name": "string"},
        "name": "",
        "photoUrls": ["string"],
        "tags": [{"id": 0,"name": "string"}],
        "status": "available"}
    create_pet_response = requests.post(endpoint + "/pett", json=payload)
#    data = create_pet_response.json()
#    pet_id = data["id"]
#    create_status = create_pet_response.status_code
#    print(f"id: {pet_id}", create_status)
    assert create_pet_response.status_code == 404
    pass
