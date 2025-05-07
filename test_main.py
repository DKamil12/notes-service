from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_note():
    response = client.post("/notes/", json={"content": "Test note"})
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["content"] == "Test note"

def test_list_notes():
    response = client.get("/notes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_note():
    # Сначала создаем
    post_response = client.post("/notes/", json={"content": "To read"})
    note_id = post_response.json()["id"]

    # Затем читаем
    get_response = client.get(f"/notes/{note_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == note_id

def test_delete_note():
    post_response = client.post("/notes/", json={"content": "To delete"})
    note_id = post_response.json()["id"]

    delete_response = client.delete(f"/notes/{note_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Note deleted"

    # Проверим, что её больше нет
    get_response = client.get(f"/notes/{note_id}")
    assert get_response.status_code == 404

def test_get_invalid_note():
    response = client.get("/notes/999999")
    assert response.status_code == 404
