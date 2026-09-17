class CarteiraDigital2:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("saldo insuficiente")

        self.saldo -= valor

class SaldoInsuficienteError(Exception):
    pass