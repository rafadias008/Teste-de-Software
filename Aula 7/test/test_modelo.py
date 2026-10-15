from src.modelo import gerar_casos,pares_de,PARAMS
from itertools import product


def test_quantidade_pairwise():
    casos = gerar_casos()

    print(f"\nQuantidade de casos: {len(casos)}")

    assert len(casos) >= 9
    assert len(casos) < 54


def test_cobertura():
    casos_totais = list(product(*PARAMS))
    casos_minimos = gerar_casos()

    pares_totais = pares_de(casos_totais)
    pares_gerados = pares_de(casos_minimos)

    assert pares_gerados == pares_totais
    assert len(pares_gerados) == 45


def test_pares_descobertos():
    casos_completos = list(product(*PARAMS))
    casos_minimos = gerar_casos()[:3]

    pares_completos = pares_de(casos_completos)
    pares_gerados = pares_de(casos_minimos)

    pares_descobertos = pares_completos - pares_gerados

    print(f"\nPares não cobertos: {len(pares_descobertos)}")
    print(f"Exemplos: {list(pares_descobertos)[:5]}")

    assert len(pares_descobertos) > 0