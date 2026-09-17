import pytest
from src.carteira_2 import CarteiraDigital2, SaldoInsuficienteError

def test_saque_saldo_insuficiente():
    carteira = CarteiraDigital2(100)

    with pytest.raises(SaldoInsuficienteError) as erro:
        carteira.sacar(150)

    assert str(erro.value) == "saldo insuficiente"

def test_saldo_nao_muda():

    carteira = CarteiraDigital2(100)

    try:
        carteira.sacar(150)
    except SaldoInsuficienteError:
        pass

    assert carteira.saldo == 100