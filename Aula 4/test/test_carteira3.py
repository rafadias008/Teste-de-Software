import pytest

from src.carteira_3 import CarteiraDigital

def test_deposito_grava_log(carteira_com_log):
    # Arrange
    carteira = carteira_com_log

    # Act
    carteira.depositar(50)

    # Assert
    with open(carteira.log_path, "r") as f:
        conteudo = f.read()

    assert conteudo == "deposito:50\n"