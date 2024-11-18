from datetime import datetime, timedelta

class GeracaoRelatorio:
    def __init__(self, gerenciamento_produto):
        self.gerenciamento_produto = gerenciamento_produto

    def relatorio_validade(self):
        # Pergunta ao usuário quantos dias considerar para validade
        dias_limite = input("Relatório de validade até quantos dias? ")
        if not dias_limite.isdigit():  # Verifica se a entrada é numérica
            print("** Valor inválido! Digite um número. **")
            return
        dias_limite = int(dias_limite)
        data_limite = datetime.now() + timedelta(days=dias_limite)  # Calcula a data limite

        produtos_validade = [
            produto for produto in self.gerenciamento_produto.produtos
            if produto.validade and datetime.now() + timedelta(days=int(produto.validade)) <= data_limite
        ]
        
        if produtos_validade:  # Verifica se há produtos com validade próxima
            print("\nProdutos com validade próxima:")
            for produto in produtos_validade:
                print(f"{produto.nome} - Validade: {produto.validade} dias")
        else:
            print("** Nenhum produto com validade próxima. **")

    def relatorio_estoque(self):
        # Pergunta ao usuário o limite de estoque para o relatório
        quantidade_limite = input("Relatório de estoque até qual quantidade? ")
        if not quantidade_limite.isdigit():  # Verifica se a entrada é numérica
            print("** Valor inválido! Digite um número. **")
            return
        quantidade_limite = int(quantidade_limite)

        produtos_estoque = [
            produto for produto in self.gerenciamento_produto.produtos
            if produto.quantidade <= quantidade_limite
        ]
        
        if produtos_estoque:  # Verifica se há produtos com estoque baixo
            print("\nProdutos com estoque baixo:")
            for produto in produtos_estoque:
                print(f"{produto.nome} - Estoque: {produto.quantidade} unidades")
        else:
            print("** Nenhum produto com estoque abaixo do limite. **")

    def menu_relatórios(self):
        # Menu principal para escolha de relatórios
        while True:
            print("\n1. Relatório de Validade\n2. Relatório de Estoque Baixo\n0. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.relatorio_validade()  # Gera relatório de validade
            elif opcao == "2":
                self.relatorio_estoque()  # Gera relatório de estoque
            elif opcao == "0":
                break  # Sai do menu
            else:
                print("** Opção inválida. **")
