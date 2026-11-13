from fastapi.testclient import TestClient
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