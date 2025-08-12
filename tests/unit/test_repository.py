import src.api.repository
import json

def test_get_user_by_id(test_app, monkeypatch):

    def mock_get_user_by_id(User, user_id):
        return {
            "id": 1,
            "name": "Lee Jong"
        }

    monkeypatch.setattr(src.api.repository, 'get_by_id', mock_get_user_by_id)

    client = test_app.test_client()
    resp = client.get("/users/1")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert "Lee Jong"  == data["name"]
    assert 1 == data["id"]

def test_get_all_users(test_app, monkeypatch):

    def mock_get_all_users(User):
        return [
            {
                "id": 1,
                "name": "Lee Jong"
            },
            {
                "id": 2,
                "name": "Dong Lee"
            }
        ]

    monkeypatch.setattr(src.api.repository, 'get_all', mock_get_all_users)

    client = test_app.test_client()
    resp = client.get("/users/")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert len(data) == 2
    assert "Lee Jong" == data[0]["name"]
    assert 1 == data[0]["id"]
    assert "Dong Lee" == data[1]["name"]
    assert 2 == data[1]["id"]

def test_create_user(test_app, monkeypatch):

    def mock_create_user(user):
        return {
                "id": 1,
                "name": "Lee Bruce"
            }

    monkeypatch.setattr(src.api.repository, 'create', mock_create_user)
    client = test_app.test_client()
    resp = client.post(
        "/users/",
        data = json.dumps({"id": 1,"name": "Lee Bruce", "password":"passw0rd"}),
        content_type="application/json"
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert "Lee Bruce"  == data["name"]
    assert 1 == data["id"]


