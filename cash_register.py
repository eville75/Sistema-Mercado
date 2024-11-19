class CashRegister:
    def __init__(self):
        self.initial_value = 0
        self.total_value = 0

    def open_cash_register(self):
        while True:
            try:
                self.initial_value = float(input("--------------------------------------------\n-> Digite o valor inicial do caixa: "))
                self.total_value = self.initial_value
                print(f"Caixa aberto com R${self.initial_value:.2f}")
                break  # Exit the loop after a valid input
            except ValueError:
                print("** Valor inválido! Digite um número válido. **")

    def close_cash_register(self):
        print(f"Valor total no caixa: R${self.total_value:.2f}")
        confirmation = input(" > Tem certeza de que deseja fechar o caixa? (sim/n): ").strip().lower()
        if confirmation == 'sim':
            print(f"  >> Caixa fechado com valor final de R${self.total_value:.2f}<< ")
            return True  # Indicate successful closure
        else:
            print("** Operação de fechamento cancelada. Voltando ao menu principal. **")
            return False  # Indicate that closure was canceled
