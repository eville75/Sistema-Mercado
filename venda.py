class GerenciamentoVenda:
    def __init__(self, gerenciamento_produto, caixa):
        self.gerenciamento_produto = gerenciamento_produto
        self.caixa = caixa  # Relacionar com o caixa principal

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
                    print("** Quantidade inválida ou maior que o disponível em estoque. **")
                    continue
                quantidade = int(quantidade)

                # Agrupar produtos no carrinho por código
                if produto.codigo in carrinho:
                    carrinho[produto.codigo]['quantidade'] += quantidade
                else:
                    carrinho[produto.codigo] = {
                        'produto': produto,
                        'quantidade': quantidade
                    }

                subtotal = produto.valor * quantidade
                total += subtotal
                print(f"Adicionado: {produto.nome} x{quantidade} - Subtotal: R${subtotal:.2f}")
            else:
                print("** Produto não encontrado! **")

        # Gerar nota fiscal
        print("\nNota Fiscal:")
        print(f"{'Produto':<20}{'Quantidade':<20}{'Subtotal':<10}")
        print("-" * 55)

        for item in sorted(carrinho.values(), key=lambda x: x['produto'].nome):
            produto = item['produto']
            quantidade = item['quantidade']
            subtotal = produto.valor * quantidade
            print(f"{produto.nome:<20}{quantidade:<20}{subtotal:<10.2f}")

        print("-" * 55)
        print(f"Total da compra: R${total:.2f}")

        confirmacao = input("Finalizar compra? (s/n): ")
        if confirmacao.lower() == 's':
            for item in carrinho.values():
                produto = item['produto']
                produto.quantidade -= item['quantidade']  # Atualizar estoque do produto

            self.caixa.valor_total += total  # Atualizar o valor do caixa principal
            print("Compra finalizada. Estoque atualizado e caixa atualizado.")
        else:
            print("Compra cancelada. Nenhuma alteração foi feita.")
