class Product:
    def __init__(self, code, name, price, expiration=None, warranty=None, quantity=0):
        self.code = code
        self.name = name
        self.price = price
        self.expiration = expiration
        self.warranty = warranty
        self.quantity = quantity


class ProductManagement:
    def __init__(self):
        self.products = []

    def register_product(self):
        print("--------------------------------------------\nTipo de produto:")
        print("1. Alimentício\n2. Utensílio\n3. Eletro")
        product_type = input("Escolha o tipo de produto (número): ")

        valid_types = {"1": "alimentício", "2": "utensílio", "3": "eletro"}
        if product_type not in valid_types:
            print("** Tipo inválido! Tente novamente. **")
            return

        code = input("Código do produto (numérico): ")
        if not code.isdigit():
            print("** Código inválido! Digite um número. Reinicie a operação. **")
            return

        name = input("Nome do produto: ")
        price = input("Valor por unidade: ")
        if not price.replace('.', '', 1).isdigit():
            print("** Valor inválido! Digite um número. **")
            return
        price = float(price)

        quantity = input("Quantidade em estoque: ")
        if not quantity.isdigit():
            print("** Quantidade inválida! Digite um número. **")
            return
        quantity = int(quantity)

        if product_type == "1":  # Alimentício
            expiration = input("Dias de validade: ")
            if not expiration.isdigit():
                print("** Valor de validade inválido! Digite um número. **")
                return
            product = Product(code, name, price, expiration=expiration, quantity=quantity)
        else:  # Utensílio ou Eletro
            warranty = input("Termo de garantia (em dias): ")
            product = Product(code, name, price, warranty=warranty, quantity=quantity)

        self.products.append(product)
        print(">> Produto cadastrado com sucesso! <<")

    def edit_product(self, product):
        print(f">> Editando {product.name}")
        new_name = input(f"Nome ({product.name}): ") or product.name
        new_price = input(f"Valor ({product.price}): ")
        new_price = float(new_price) if new_price else product.price
        new_quantity = input(f"Quantidade ({product.quantity}): ")
        new_quantity = int(new_quantity) if new_quantity else product.quantity

        product.name = new_name
        product.price = new_price
        product.quantity = new_quantity
        print(">> Produto editado com sucesso! <<")

    def remove_product(self):
        product = self.search_product()
        if product:
            confirmation = input(f" > Tem certeza de que deseja remover {product.name}? (s/n): ")
            if confirmation.lower() == 's':
                self.products.remove(product)
                print(">> Produto removido com sucesso. <<")
            else:
                print(">> Remoção cancelada. <<")

    def search_product(self, term=None):
        if term is None:
            term = input("--------------------------------------------\nDigite o código ou nome do produto: ").strip().lower()

        for product in self.products:
            if term == str(product.code) or term in product.name.lower():
                print(f">> Produto encontrado: {product.name}, Estoque: {product.quantity}, Valor: {product.price:.2f}. <<")
                return product

        print(">> Produto não encontrado. <<")
        return None

    def product_menu(self):
        while True:
            print("--------------------------------------------\n1. Cadastrar Produto\n2. Buscar Produto\n3. Editar Produto\n4. Remover Produto\n0. Voltar")
            option = input("-> Escolha uma opção: ")
            if option == "1":
                self.register_product()
            elif option == "2":
                self.search_product()
            elif option == "3":
                product = self.search_product()
                if product:
                    self.edit_product(product)
            elif option == "4":
                self.remove_product()
            elif option == "0":
                break
            else:
                print("** Opção inválida. Tente novamente. **")
