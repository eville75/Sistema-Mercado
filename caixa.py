class Caixa:
    def __init__(self):
        self.valor_inicial = 0
        self.valor_total = 0

    def abrir_caixa(self):
        while True:
            try:
                self.valor_inicial = float(input("-----------------------------------\nDigite o valor inicial do caixa: "))
                self.valor_total = self.valor_inicial
                print(f"Caixa aberto com R${self.valor_inicial}")
                break  # Sai do loop após uma entrada válida
            except ValueError:
                print("** Valor inválido! Digite um número válido. **")

    def fechar_caixa(self):
        if self.valor_total > 0:
            print(f"Caixa fechado com valor final de R${self.valor_total}")
        else:
            print("** Erro ao fechar o caixa. Voltando ao menu principal. **")
            return False  # Retorna um indicador de que o fechamento falhou
