class GerenciamentoVenda:
    def __init__(self, gerenciamento_produto):
        self.gerenciamento_produto = gerenciamento_produto

    def nova_venda(self):
        total = 0
        carrinho = {}

        while True:
            codigo = input("Digite o código do produto (ou '0' para finalizar): ")
            if codigo == "0":
                break

            produto = self.gerenciamento_produto.buscar_produto()
            if produto:
                quantidade = input("Quantidade: ")
                if not quantidade.isdigit() or int(quantidade) > produto.quantidade:
                    print("Quantidade inválida ou maior que o disponível em estoque.")
                    continue
                quantidade = int(quantidade)

                # Agrupamento de produtos
                if codigo in carrinho:
                    carrinho[codigo]['quantidade'] += quantidade
                else:
                    carrinho[codigo] = {'produto': produto, 'quantidade': quantidade}

                subtotal = produto.valor * quantidade
                total += subtotal
                print(f"Adicionado: {produto.nome} x{quantidade} - Subtotal: R${subtotal}")

        print("\nResumo da venda:")
        for item in carrinho.values():
            produto = item['produto']
            quantidade = item['quantidade']
            subtotal = produto.valor * quantidade
            print(f"{produto.nome} x{quantidade} - Subtotal: R${subtotal}")

        print(f"Total da compra: R${total}")

        # Confirmar finalização
        confirmacao = input("Finalizar compra? (s/n): ")
        if confirmacao.lower() == 's':
            for item in carrinho.values():
                item['produto'].quantidade -= item['quantidade']
            print("Compra finalizada e estoque atualizado.")
