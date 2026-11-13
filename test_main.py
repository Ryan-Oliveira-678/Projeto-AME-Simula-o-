from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_consultar_familia_bloqueada():
    response = client.get("/api/familias/12345678900")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "BLOQUEADO"

def test_consultar_familia_liberada():
    response = client.get("/api/familias/98765432100")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "LIBERADO"
