from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Projeto AME Hoje - MVP",
    description="API para controle de distribuição de cestas básicas e prevenção de duplicidade.",
    version="1.0.0"
)

<<<<<<< HEAD
# Base de dados simulada para o MVP do Projeto AME Hoje
=======
>>>>>>> 4a0b2c75a0a84e3e81306e5eda6ba82118b44c1f
FAMILIAS_DB = {
    "12345678900": {
        "nome": "Maria da Silva Santos",
        "bairro": "Jardim das Palmeiras",
        "recebeu_este_mes": True,
        "data_entrega": "12/11/2026",
        "voluntario": "Voluntario Carlos"
    },
    "98765432100": {
        "nome": "Jose Oliveira Souza",
        "bairro": "Jardim Benfica",
        "recebeu_este_mes": False,
        "data_entrega": None,
        "voluntario": None
    }
}

<<<<<<< HEAD
def read_root():
    return {"status": "online", "projeto": "Projeto AME Hoje MVP"}

def consultar_familia(cpf: str):
    """
    Valida o histórico de entrega do mês e aplica a regra de bloqueio de duplicidade (RF04).
    """
    familia = FAMILIAS_DB.get(cpf)
    if not familia:
        return {
            "status": "ERRO",
            "mensagem": "Cadastro não encontrado para o CPF informado."
        }
=======
class ConsultaResponse(BaseModel.model_config = {**BaseModel.model_config}):
    pass

@app.get("/")
def read_root():
    return {"status": "online", "projeto": "Projeto AME Hoje MVP"}

@app.get("/api/familias/{cpf}")
def consultar_familia(cpf: str):
    """
    Realiza a busca da família por CPF e valida o histórico de entrega do mês.
    Implementa a regra de bloqueio de duplicidade (RF04).
    """
    familia = FAMILIAS_DB.get(cpf)
    if not familia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cadastro não encontrado para o CPF informado."
        )
>>>>>>> 4a0b2c75a0a84e3e81306e5eda6ba82118b44c1f
    
    if familia["recebeu_este_mes"]:
        return {
            "status": "BLOQUEADO",
            "mensagem": "Atenção: A família já recebeu cesta básica neste mês de referência.",
            "dados": familia
        }
    
    return {
        "status": "LIBERADO",
        "mensagem": "Família liberada para retirada da cesta básica.",
        "dados": familia
<<<<<<< HEAD
    }
=======
    }
>>>>>>> 4a0b2c75a0a84e3e81306e5eda6ba82118b44c1f
