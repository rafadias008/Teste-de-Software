from itertools import product


def regra(cartao, documento, grupo_chamado, prioridade):
    return cartao and documento and (grupo_chamado or prioridade)


def pares_independentes(decisao, n):
    linhas = list(product((False, True), repeat=n))
    indices = {linha: indice for indice, linha in enumerate(linhas)}
    pares = {condicao: [] for condicao in range(n)}

    for linha in linhas:
        for condicao in range(n):
            if linha[condicao]:
                continue

            alterada = list(linha)
            alterada[condicao] = True
            alterada = tuple(alterada)

            if decisao(*linha) != decisao(*alterada):
                pares[condicao].append((indices[linha], indices[alterada]))

    return pares