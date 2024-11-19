class SaleManagement:
    def __init__(self, product_management, cash_register):
        self.product_management = product_management
        self.cash_register = cash_register  # Link to the main cash register

    def new_sale(self):
        total = 0
        cart = {}

        while True:
            code = input("Digite o código do produto (ou '0' para finalizar): ").strip()
            if code == "0":
                break

            product = self.product_management.search_product(code)  # Pass the code directly
            if product:
                quantity = input("Quantidade: ").strip()
                if not quantity.isdigit() or int(quantity) > product.quantity:
                    print("** Quantidade inválida ou maior que o disponível em estoque. **")
                    continue
                quantity = int(quantity)

                # Group products in the cart by code
                if product.code in cart:
                    cart[product.code]['quantity'] += quantity
                else:
                    cart[product.code] = {
                        'product': product,
                        'quantity': quantity
                    }

                subtotal = product.price * quantity
                total += subtotal
                print(f"Adicionado: {product.name} x{quantity} - Subtotal: R${subtotal:.2f}")
            else:
                print("** Produto não encontrado! **")

        # Generate the invoice
        print("\nNota Fiscal:")
        print(f"{'Produto':<20}{'Quantidade':<20}{'Subtotal':<10}")
        print("-" * 55)

        for item in sorted(cart.values(), key=lambda x: x['product'].name):
            product = item['product']
            quantity = item['quantity']
            subtotal = product.price * quantity
            print(f"{product.name:<20}{quantity:<20}{subtotal:<10.2f}")

        print("-" * 55)
        print(f"Total da compra: R${total:.2f}")

        confirmation = input("Finalizar compra? (s/n): ").strip().lower()
        if confirmation == 's':
            for item in cart.values():
                product = item['product']
                product.quantity -= item['quantity']  # Update product stock

            self.cash_register.total_value += total  # Update the main cash register's total value
            print("Compra finalizada. Estoque atualizado e caixa atualizado.")
        else:
            print("Compra cancelada. Nenhuma alteração foi feita.")
