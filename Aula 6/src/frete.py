
class frete:
    def __init__(self, valor_compra, cliente_premium, peso):
        self.valor_compra = valor_compra
        self.cliente_premium = cliente_premium
        self.peso = peso

    def frete(self):
        return self.valor_compra >= 200 and self.cliente_premium and self.peso <= 30