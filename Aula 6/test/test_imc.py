import pytest

from src.imc import imc

#Exercicio 1
def test_calcular_imc():
    assert imc(70, 1.75).calcular_imc() == pytest.approx(70 / 1.75**2)


@pytest.mark.parametrize(
    "valor_imc, categorizacao",
    [
        (18.499, "Abaixo do Peso"),
        (18.5, "Peso Normal"),
        (24.999, "Peso Normal"),
        (25, "Sobrepeso"),
        (29.999, "Sobrepeso"),
        (30, "Obesidade"),
    ],

    ids=[
        "CE1",
        "CE2",
        "CE3",
        "CE4",
        "CE5",
        "CE6",
    ],
)
def test_categorizar_imc(valor_imc, categorizacao):
    assert imc.categorizar_imc(valor_imc) == categorizacao


def test_calcular_imc_rejeita_peso_menor_zero():
    with pytest.raises(ValueError):
        imc(0, 1.75).calcular_imc()


def test_calcular_imc_rejeita_altura_menor_zero():
    with pytest.raises(ValueError):
        imc(70, 0).calcular_imc()


@pytest.mark.parametrize(
    "peso, altura, categorizacao",
    [
        (50, 1.70, "Abaixo do Peso"),
        (68, 1.70, "Peso Normal"),
        (78, 1.70, "Sobrepeso"),
        (90, 1.70, "Obesidade"),
    ],
)
def test_classificar_pessoa(peso, altura, categorizacao):
    assert imc(peso, altura).classificar_pessoa() == categorizacao

#Fim Exercicio 1 e 2