from math import inf

from src.faixas import classificar_por_faixas


class imc:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        if self.peso <= 0 or self.altura <= 0:
            raise ValueError("Peso e altura devem ser positivos.")
        return self.peso / self.altura**2

    @staticmethod
    def categorizar_imc(imc):
        faixas = [
            (18.5, "Abaixo do Peso"),
            (25, "Peso Normal"),
            (30, "Sobrepeso"),
            (inf, "Obesidade"),
        ]
        return classificar_por_faixas(imc, faixas)

    def classificar_pessoa(self):
        return self.categorizar_imc(self.calcular_imc())