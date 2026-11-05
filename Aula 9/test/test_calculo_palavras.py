import pytest
from calculo_palavras import contar_palavras

def test_contar_palavras():
    assert contar_palavras("Olá, mundo!") == 2
    # assert contar_palavras("Esta é uma frase com várias palavras.") == 7

