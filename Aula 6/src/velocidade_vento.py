from math import inf

from src.faixas import classificar_por_faixas


class vento:

    def __init__(self, velocidade):
        self.velocidade = velocidade

    def classificar_vento(self, velocidade):    
        faixas = [
            (20, "Calmo"),
            (40, "Moderado"),
            (60, "Forte"),
            (inf, "Tempestade"),
        ]
        return classificar_por_faixas(velocidade, faixas)