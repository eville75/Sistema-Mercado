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
        print("----------------------------\nTipo de produto:")
        print("1. Alimentício\n2. Utensílio\n3. Eletro")
        tipo = input("Escolha o tipo de produto (número): ")

        tipos_validos = {"1": "alimentício", "2": "utensílio", "3": "eletro"}
        if tipo not in tipos_validos:
            print("** Tipo inválido! Tente novamente. **")
            return

        codigo = input("Código do produto (numérico): ")
        if not codigo.isdigit():
            print("** Código inválido! Digite um número. Reinicie a operação. **")
            return

        nome = input("Nome do produto: ")
        valor = input("Valor por unidade: ")
        if not valor.replace('.', '', 1).isdigit():
            print("** Valor inválido! Digite um número. **")
            return
        valor = float(valor)

        quantidade = input("Quantidade em estoque: ")
        if not quantidade.isdigit():
            print("** Quantidade inválida! Digite um número. **")
            return
        quantidade = int(quantidade)

        if tipo == "1":  # Alimentício
            validade = input("Dias de validade: ")
            if not validade.isdigit():
                print("** Valor de validade inválido! Digite um número. **")
                return
            produto = Produto(codigo, nome, valor, validade=validade, quantidade=quantidade)
        else:  # Utensílio ou Eletro
            garantia = input("Termo de garantia (em dias): ")
            produto = Produto(codigo, nome, valor, garantia=garantia, quantidade=quantidade)

        self.produtos.append(produto)
        print(">> Produto cadastrado com sucesso! <<")

    def editar_produto(self, produto):
        print(f">> Editando {produto.nome}")
        novo_nome = input(f"Nome ({produto.nome}): ") or produto.nome
        novo_valor = input(f"Valor ({produto.valor}): ")
        novo_valor = float(novo_valor) if novo_valor else produto.valor
        nova_quantidade = input(f"Quantidade ({produto.quantidade}): ")
        nova_quantidade = int(nova_quantidade) if nova_quantidade else produto.quantidade

        produto.nome = novo_nome
        produto.valor = novo_valor
        produto.quantidade = nova_quantidade
        print(">> Produto editado com sucesso! <<")

    def remover_produto(self):
        produto = self.buscar_produto()
        if produto:
            confirmacao = input(f" > Tem certeza de que deseja remover {produto.nome}? (s/n): ")
            if confirmacao.lower() == 's':
                self.produtos.remove(produto)
                print(">> Produto removido com sucesso. <<")
            else:
                print(">> Remoção cancelada. <<")

    def buscar_produto(self, termo=None):
        if termo is None:  # Permitir que um código seja passado diretamente
            termo = input("----------------------------\nDigite o código ou nome do produto: ").strip().lower()

        for produto in self.produtos:
            # Comparar código como string e realizar busca case-insensitive no nome
            if termo == str(produto.codigo) or termo in produto.nome.lower():
                print(f">> Produto encontrado: {produto.nome}, Estoque: {produto.quantidade}, Valor: {produto.valor:.2f}. <<")
                return produto

        print(">> Produto não encontrado. <<")
        return None

    def menu_produtos(self):
        while True:
            print("----------------------------\n1. Cadastrar Produto\n2. Buscar Produto\n3. Editar Produto\n4. Remover Produto\n0. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.cadastrar_produto()
            elif opcao == "2":
                self.buscar_produto()
            elif opcao == "3":
                produto = self.buscar_produto()
                if produto:
                    self.editar_produto(produto)
            elif opcao == "4":
                self.remover_produto()
            elif opcao == "0":
                break
            else:
                print("** Opção inválida. Tente novamente. **")
