from fastapi.testclient import TestClient
<<<<<<< HEAD
from main import read_root, consultar_familia

def test_read_root():
    response = read_root()
    assert response["status"] == "online"
    assert response["projeto"] == "Projeto AME Hoje MVP"

def test_consultar_familia_bloqueada():
    # Testa a regra de bloqueio de duplicidade para o CPF que já recebeu
    response = consultar_familia("12345678900")
    assert response["status"] == "BLOQUEADO"

def test_consultar_familia_liberada():
    # Testa a liberação para o CPF que ainda não recebeu no mês
    response = consultar_familia("98765432100")
    assert response["status"] == "LIBERADO"
=======
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
>>>>>>> 4a0b2c75a0a84e3e81306e5eda6ba82118b44c1f
