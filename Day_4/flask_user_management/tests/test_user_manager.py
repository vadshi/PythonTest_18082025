import json


def test_add_user(test_client, user_payload):
    response = test_client.post(
        "/users", data=json.dumps(user_payload), content_type = "application/json"
    )

    assert response.status_code == 201
    create_response_json = json.loads(response.data)
    assert create_response_json.keys() == dict(message="User created").keys() 
    assert "User created with id" in create_response_json.get("message")

    response = test_client.get("/users")
    assert response.status_code == 200

    read_response_json = json.loads(response.data)
    print(f'{read_response_json = }')
    assert len(read_response_json) == 1