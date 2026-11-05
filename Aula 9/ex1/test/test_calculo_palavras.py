import pytest
from calculo_palavras import contar_palavras

def test_contar_palavras():
    assert contar_palavras("Dia dia DIA") == {"dia": 3}
    assert contar_palavras("fim. Fim!") == {"fim": 2}
    assert contar_palavras("bom\ndia") == {"bom": 1, "dia": 1}
    assert contar_palavras("dia a dia") == {"dia": 2, "a": 1}
