import pytest
from src.entrega import frete,frete_corrigido,gerar_casos_frete,PARAMS
from itertools import product

casos = gerar_casos_frete()

@pytest.mark.parametrize(
    "peso, urgencia, seguro, regiao",
    casos
)

def test_frete_pairwise(peso, urgencia, seguro, regiao):
    resultado = frete(peso, urgencia, seguro, regiao)
    valor_esperado = frete_corrigido(peso, urgencia, seguro, regiao)

    assert resultado == valor_esperado


# def test_frete_completo(peso, urgencia, seguro, regiao):
#     resultado = frete(peso, urgencia, seguro, regiao)
#     valor_esperado = frete_corrigido(peso, urgencia, seguro, regiao)

#     assert resultado == valor_esperado


@pytest.mark.parametrize(
    "peso, urgencia, seguro, regiao",
    list(product(*PARAMS))
)

def test_frete_completo_36(peso, urgencia, seguro, regiao):
    resultado = frete(peso, urgencia, seguro, regiao)
    valor_esperado = frete_corrigido(peso, urgencia, seguro, regiao)

    assert resultado == valor_esperado

