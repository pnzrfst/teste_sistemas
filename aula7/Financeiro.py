class Financeiro:
    def __init__(self):
        self.valor_devido = 0
        self.valor_pago = 0

    def adicionar_valor_devido(self, valor):
        self.valor_devido += valor

    def adicionar_valor_pago(self, valor):
        self.valor_pago += valor

    def calcular_valor_em_aberto(self):
        return self.valor_devido - self.valor_pago