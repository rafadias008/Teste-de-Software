import pytest
from src.carteira import CarteiraDigital


def test_saldo_inicial_0():
    carteira = CarteiraDigital()

    saldo = carteira.saldo

    assert saldo == 0


def test_saldo_inicial_informado():
    carteira = CarteiraDigital(70)

    saldo = carteira.saldo

    assert saldo == 70


def test_depositar_valor():
    carteira = CarteiraDigital(100)

    carteira.depositar(50)

    assert carteira.saldo == 150


def test_sacar_valor_dentro_do_saldo():
    carteira = CarteiraDigital(100)

    carteira.sacar(80)

    assert carteira.saldo == 20