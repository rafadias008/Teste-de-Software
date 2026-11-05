

# Devolve um dict: cada palavra e o seu número de ocorrências
# Espaços e quebras de linha separam as palavras; hífen interno faz parte da
# palavra
# Maiúsculas contam como minúsculas; os sinais .,;:!? nas bordas da palavra
# são ignorados

def contar_palavras(texto):

    ocorrencias = {}
    for palavra in texto.split():
        palavra = palavra.strip(".,;:!?").lower()
        if palavra:
            if palavra in ocorrencias:
                ocorrencias[palavra] += 1
            else:
                ocorrencias[palavra] = 1
    return ocorrencias