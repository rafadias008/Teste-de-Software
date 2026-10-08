import pytest

from src.frete import frete


@pytest.mark.parametrize(
    "valor, status_cliente, peso, frete_esperado",
    [
        (200, True, 30, True),
        (200, True, 30.01, False),
        (200, False, 30, False),
        (200, False, 30.01, False),
        (199.99, True, 30, False),
        (199.99, True, 30.01, False),
        (199.99, False, 30, False),
        (199.99, False, 30.01, False),
    ],
    ids=["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"],
)
def test_tem_frete(
    valor, status_cliente, peso, frete_esperado
):
    assert (
        frete(valor, status_cliente, peso).frete()
        is frete_esperado
    )