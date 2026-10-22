import pytest

from src.preco import preco_final


@pytest.mark.parametrize(
    ("preco", "vip", "esperado"),
    [
        (100, False, 100),
        (40, False, 50),
        (200, True, 160),
        (40, True, 50),
    ],
    ids=["sem-vip-acima-minimo", "sem-vip-abaixo-minimo", "vip-sem-piso", "vip-com-piso"],
)
def test_pares_definicao_uso(preco, vip, esperado):
    assert preco_final(preco, vip) == esperado