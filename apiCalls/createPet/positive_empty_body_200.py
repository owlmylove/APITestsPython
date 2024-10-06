import requests

endpoint = "https://petstore.swagger.io/v2"


# Create a new pet
def test_create_pet():
    payload = {}
    create_pet_response = requests.post(endpoint + "/pet", json=payload)
    data = create_pet_response.json()
    pet_id = data["id"]
    status = create_pet_response.status_code
    print(f"id: {pet_id}")
    print(data, status)
    assert create_pet_response.status_code == 200
    pass
