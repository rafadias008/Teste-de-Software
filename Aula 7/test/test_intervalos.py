from hypothesis import given, strategies as st
from src.intervalos import mesclar, normalizar

entradas = st.lists(
    st.tuples(
        st.integers(min_value=0, max_value=50),
        st.integers(min_value=0, max_value=50)
    )
)


# Propriedade 1: idempotência
@given(entradas)
def test_idempotencia(intervalos):
    intervalos = normalizar(intervalos)

    resultado = mesclar(intervalos)

    assert mesclar(resultado) == resultado


# Propriedade 2: ordem e ausência de sobreposição
@given(entradas)
def test_ordem_sem_sobreposicao(intervalos):
    intervalos = normalizar(intervalos)

    resultado = mesclar(intervalos)

    for ini, fim in resultado:
        assert ini <= fim

    for i in range(len(resultado) - 1):
        assert resultado[i][1] < resultado[i + 1][0]


# Propriedade 3: todos os intervalos estão contidos
@given(entradas)
def test_contencao(intervalos):
    intervalos = normalizar(intervalos)

    resultado = mesclar(intervalos)

    for ini, fim in intervalos:
        assert any(
            r_ini <= ini and fim <= r_fim
            for r_ini, r_fim in resultado
        )