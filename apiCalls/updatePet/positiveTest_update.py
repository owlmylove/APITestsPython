import requests

endpoint = "https://petstore.swagger.io/v2"


# Update existing pet
def test_update_pet():
    payload = {
        "id": 898080,
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

# during update generating of random ID works with different logic
# from when we create a new pet it can be +1, + 2, +5, +30 or even minus
# maybe it the logic of rand gen

# during update endpoint we can use the same tests as for POST,
# just to be sure endpoint works as expected
# there is nothing we can test that this endpoint does different from POST,
# even ID could be used with random non-existing number,
# as there is no any validation on existence
