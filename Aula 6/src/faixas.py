def classificar_por_faixas(valor, faixas):
    for limite_superior, rotulo in faixas:
        if valor < limite_superior:
            return rotulo
    raise ValueError("O valor não pertence a nenhuma faixa.")