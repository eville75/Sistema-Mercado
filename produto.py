class Produto:
    def __init__(self, codigo, nome, valor, validade=None, garantia=None, quantidade=0):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.validade = validade
        self.garantia = garantia
        self.quantidade = quantidade

class GerenciamentoProduto:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self):
        tipo = input("----------------------------\nTipo de produto (alimentício/utensílio/eletro): ").lower()
        if tipo not in ["alimentício", "utensílio", "eletro"]:
            print("Tipo inválido! Tente novamente.")
            return

        codigo = input("Código do produto (numérico): ")
        if not codigo.isdigit():
            print("Código inválido! Digite um número.")
            return

        nome = input("Nome do produto: ")
        valor = input("Valor por unidade: ")
        if not valor.replace('.', '', 1).isdigit():
            print("Valor inválido! Digite um número.")
            return
        valor = float(valor)
        
        quantidade = input("Quantidade em estoque: ")
        if not quantidade.isdigit():
            print("Quantidade inválida! Digite um número.")
            return
        quantidade = int(quantidade)

        if tipo == "alimentício":
            validade = input("Dias de validade: ")
            if not validade.isdigit():
                print("Valor de validade inválido! Digite um número.")
                return
            produto = Produto(codigo, nome, valor, validade=validade, quantidade=quantidade)
        else:
            garantia = input("Termo de garantia: ")
            produto = Produto(codigo, nome, valor, garantia=garantia, quantidade=quantidade)

        self.produtos.append(produto)
        print("Produto cadastrado com sucesso!")

    def remover_produto(self):
        produto = self.buscar_produto()
        if produto:
            confirmacao = input(f"Tem certeza de que deseja remover {produto.nome}? (s/n): ")
            if confirmacao.lower() == 's':
                self.produtos.remove(produto)
                print("Produto removido com sucesso.")
            else:
                print("Remoção cancelada.")

    def buscar_produto(self):
        termo = input("----------------------------\nDigite o código ou nome do produto: ").lower()
        for produto in self.produtos:
            if termo in produto.nome.lower() or termo == produto.codigo:
                print(f"Produto encontrado: {produto.nome}, Estoque: {produto.quantidade}")
                return produto
        print("Produto não encontrado.")
        return None

    def menu_produtos(self):
        while True:
            print("----------------------------\n1. Cadastrar Produto\n2. Buscar Produto\n3. Remover Produto\n4. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.cadastrar_produto()
            elif opcao == "2":
                self.buscar_produto()
            elif opcao == "3":
                self.remover_produto()
            elif opcao == "4":
                break
            else:
                print("Opção inválida. Tente novamente.")
