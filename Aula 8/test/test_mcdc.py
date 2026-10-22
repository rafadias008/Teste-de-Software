from itertools import product

import pytest

from src.embarque import pode_embarcar, pode_embarcar_defeituosa
from src.mcdc import pares_independentes, regra


LINHAS = list(product((False, True), repeat=4))
CONJUNTOS_MINIMOS = [
    ("M1-nao-detecta", (12, 14, 13, 6, 10), False),
    ("M2-detecta", (12, 14, 13, 6, 9), True),
    ("M3-detecta", (12, 14, 13, 5, 10), True),
    ("M4-detecta", (12, 14, 13, 5, 9), True),
]


def test_quantidade_de_pares_independentes():
    pares = pares_independentes(regra, 4)

    assert {condicao: len(lista) for condicao, lista in pares.items()} == {
        0: 3,
        1: 3,
        2: 1,
        3: 1,
    }
    assert pares == {
        0: [(5, 13), (6, 14), (7, 15)],
        1: [(9, 13), (10, 14), (11, 15)],
        2: [(12, 14)],
        3: [(12, 13)],
    }


def test_extremos_todos_verdadeiros():
    entrada = (True, True, True, True)

    assert regra(*entrada) is True
    assert pode_embarcar_defeituosa(*entrada) == regra(*entrada)
    assert pode_embarcar(*entrada) == regra(*entrada)


def test_extremos_todos_falsos():
    entrada = (False, False, False, False)

    assert regra(*entrada) is False
    assert pode_embarcar_defeituosa(*entrada) == regra(*entrada)
    assert pode_embarcar(*entrada) == regra(*entrada)


@pytest.mark.parametrize(
    ("nome", "indices", "defeito_detectado"),
    CONJUNTOS_MINIMOS,
    ids=[caso[0] for caso in CONJUNTOS_MINIMOS],
)
def test_conjuntos_mcdc_minimos(nome, indices, defeito_detectado):
    entradas = [LINHAS[indice] for indice in indices]
    diferencas = [
        regra(*entrada) != pode_embarcar_defeituosa(*entrada)
        for entrada in entradas
    ]

    assert any(diferencas) is defeito_detectado
    assert all(pode_embarcar(*entrada) == regra(*entrada) for entrada in entradas)