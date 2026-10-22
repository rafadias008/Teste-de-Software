import pytest

from src.forca import forca


@pytest.mark.parametrize(
    ("senha", "esperado"),
    [
        ("abc", "fraca"),
        ("abcdefgh", "media"),
        ("1abcdefg", "media"),
        ("!abcdefg", "media"),
        ("1234abcd", "forte"),
        ("!!!abcdef", "forte"),
    ],
    ids=["curta", "base-letras", "digito-sem-limiar", "simbolo-sem-limiar", "forte-digitos", "forte-simbolos"],
)

def test_caminhos_base(senha, esperado):
    assert forca(senha) == esperado


@pytest.mark.parametrize(
    ("senha", "esperado"),
    [
        ("abcdefgh", "media"),
        ("abcdefghi", "media"),
        ("abcdefghijklmnopqrst", "media"),
    ],
    ids=["8-iteracoes", "9-iteracoes", "20-iteracoes"],
)
def test_voltas_do_laco(senha, esperado):
    assert forca(senha) == esperado