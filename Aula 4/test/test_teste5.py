import pytest

from src.teste5 import transferir
from src.carteira_2 import SaldoInsuficienteError


@pytest.mark.parametrize(
    "valor",
    [100, 250, 500],
    ids=[
        "transferencia-100",
        "transferencia-250",
        "transferencia-500",
    ]
)
def test_transferencia_bem_sucedida(duas_carteiras, valor):
    # Arrange
    origem, destino = duas_carteiras

    # Act
    transferir(origem, destino, valor)

    # Assert
    assert origem.saldo == 1000 - valor
    assert destino.saldo == valor

def test_transferencia_sem_saldo_nao_altera_carteiras(duas_carteiras):
    # Arrange
    origem, destino = duas_carteiras

    saldo_origem_antes = origem.saldo
    saldo_destino_antes = destino.saldo

    # Act
    with pytest.raises(SaldoInsuficienteError):
        transferir(origem, destino, 1500)

    # Assert
    assert origem.saldo == saldo_origem_antes
    assert destino.saldo == saldo_destino_antes