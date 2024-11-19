class Caixa:
    def __init__(self):
        self.valor_inicial = 0
        self.valor_total = 0

    def abrir_caixa(self):
        while True:
            try:
                self.valor_inicial = float(input("-----------------------------------\nDigite o valor inicial do caixa: "))
                self.valor_total = self.valor_inicial
                print(f"Caixa aberto com R${self.valor_inicial:.2f}")
                break  # Sai do loop após uma entrada válida
            except ValueError:
                print("** Valor inválido! Digite um número válido. **")

    def fechar_caixa(self):
        print(f"Valor total no caixa: R${self.valor_total:.2f}")
        confirmacao = input(" > Tem certeza de que deseja fechar o caixa? (sim/n): ").strip().lower()
        if confirmacao == 'sim':
            print(f"  >> Caixa fechado com valor final de R${self.valor_total:.2f}<< ")
            return True  # Indicador de sucesso no fechamento
        else:
            print("** Operação de fechamento cancelada. Voltando ao menu principal. **")
            return False  # Indicador de que o fechamento foi cancelado
