import pytest

from src.velocidade_vento import vento


@pytest.mark.parametrize(
    "velocidade, classificacao",
    [
        (19.999, "Calmo"),
        (20, "Moderado"),
        (39.999, "Moderado"),
        (40, "Forte"),
        (59.999, "Forte"),
        (60, "Tempestade"),
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
def test_classificar_vento_nas_fronteiras(velocidade, classificacao):
    assert vento(velocidade).classificar_vento(velocidade) == classificacao