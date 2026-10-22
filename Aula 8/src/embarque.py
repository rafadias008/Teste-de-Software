def pode_embarcar(cartao, documento, grupo_chamado, prioridade):
    return cartao and documento and (grupo_chamado or prioridade)


def pode_embarcar_defeituosa(cartao, documento, grupo_chamado, prioridade):
    return cartao and documento and grupo_chamado or prioridade