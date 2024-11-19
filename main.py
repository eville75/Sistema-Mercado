from cash_register import CashRegister
from product import ProductManagement
from sale import SaleManagement
from report import ReportGeneration

def start_system():
    cash_register = CashRegister()
    products = ProductManagement()
    sales = SaleManagement(products, cash_register)  # Pass the cash register to SaleManagement
    reports = ReportGeneration(products)

    cash_register.open_cash_register()
    while True:
        print("--------------------------------------------\nMenu Principal:")
        print("1. Cadastro de Produtos")
        print("2. Nova Venda")
        print("3. Relatórios")
        print("4. Fechar Caixa")
        option = input("-> Escolha uma opção: ")

        if option == "1":
            products.product_menu()
        elif option == "2":
            sales.new_sale()
        elif option == "3":
            reports.report_menu()
        elif option == "4":
            if not cash_register.close_cash_register():
                continue  # Return to the main menu if closing fails
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    start_system()
