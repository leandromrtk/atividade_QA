from fastapi.testclient import TestClient
from main import app, Item

client = TestClient(app)

def test_post_item():
    # Testando a criação de um item
    response = client.post("/items/", json={"id": 1, "name": "Item 1", "description": "Descrição do Item 1"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Item 1", "description": "Descrição do Item 1"}
    
def test_get_item():
    # Testando a recuperação de todos os itens
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json() == [{"id": 1, "name": "Item 1", "description": "Descrição do Item 1"}]
    
def test_post_item_duplicate_id():
    # Testando a criação de um item com ID duplicado
    response = client.post("/items/", json={"id": 1, "name": "Item 2", "description": "Descrição do Item 2"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Item já existente."}