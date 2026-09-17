import pytest

from src.teste5 import transferir


@pytest.fixture
def duas_carteiras():
    origem = transferir(1000)
    destino = transferir(0)
    
    return origem, destino