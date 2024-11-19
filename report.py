from datetime import datetime, timedelta

class ReportGeneration:
    def __init__(self, product_management):
        self.product_management = product_management

    def expiration_report(self):
        # Ask the user how many days to consider for expiration
        days_limit = input("--------------------------------------------\n> Relatório de validade até quantos dias? ")
        if not days_limit.isdigit():  # Check if the input is numeric
            print("** Valor inválido! Digite um número. **")
            return
        days_limit = int(days_limit)
        limit_date = datetime.now() + timedelta(days=days_limit)  # Calculate the limit date

        products_expiration = [
            product for product in self.product_management.products
            if product.expiration and datetime.now() + timedelta(days=int(product.expiration)) <= limit_date
        ]
        
        if products_expiration:  # Check if there are products with approaching expiration dates
            print("\n>> Produtos com validade próxima:")
            for product in products_expiration:
                print(f"{product.name} - Validade: {product.expiration} dias")
        else:
            print("** Nenhum produto com validade próxima. **")

    def stock_report(self):
        # Ask the user the stock limit for the report
        quantity_limit = input("--------------------------------------------\n> Relatório de estoque até qual quantidade? ")
        if not quantity_limit.isdigit():  # Check if the input is numeric
            print("** Valor inválido! Digite um número. **")
            return
        quantity_limit = int(quantity_limit)

        products_stock = [
            product for product in self.product_management.products
            if product.quantity <= quantity_limit
        ]
        
        if products_stock:  # Check if there are products with low stock
            print("--------------------------------------------\nProdutos com estoque baixo:")
            for product in products_stock:
                print(f"{product.name} - Estoque: {product.quantity} unidades")
        else:
            print("** Nenhum produto com estoque abaixo do limite. **")

    def report_menu(self):
        # Main menu for report selection
        while True:
            print("--------------------------------------------\n1. Relatório de Validade\n2. Relatório de Estoque Baixo\n0. Voltar")
            option = input("-> Escolha uma opção: ")
            if option == "1":
                self.expiration_report()  # Generate expiration report
            elif option == "2":
                self.stock_report()  # Generate stock report
            elif option == "0":
                break  # Exit the menu
            else:
                print("** Opção inválida. **")
