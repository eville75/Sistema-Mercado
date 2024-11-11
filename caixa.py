class Caixa:
    def __init__(self):
        self.valor_inicial = 0
        self.valor_total = 0

    def abrir_caixa(self):
        self.valor_inicial = float(input("-----------------------------------\nDigite o valor inicial do caixa: "))
        self.valor_total = self.valor_inicial
        print(f"Caixa aberto com R${self.valor_inicial}")

    def fechar_caixa(self):
        print(f"Caixa fechado com valor final de R${self.valor_total}")
