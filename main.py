from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Projeto AME Hoje - MVP",
    description="API para controle de distribuição de cestas básicas e prevenção de duplicidade.",
    version="1.0.0"
)

# Base de dados simulada para o MVP do Projeto AME Hoje
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
    }