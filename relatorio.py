from datetime import datetime, timedelta

class GeracaoRelatorio:
    def __init__(self, gerenciamento_produto):
        self.gerenciamento_produto = gerenciamento_produto

    def relatorio_validade(self):
        dias_limite = input("Relatório de validade até quantos dias? ")
        if not dias_limite.isdigit():
            print("** Valor inválido! Digite um número. **")
            return
        dias_limite = int(dias_limite)
        data_limite = datetime.now() + timedelta(days=dias_limite)

        for produto in self.gerenciamento_produto.produtos:
            if produto.validade and datetime.now() + timedelta(days=int(produto.validade)) <= data_limite:
                print(f"{produto.nome} - Validade: {produto.validade} dias")

    def relatorio_estoque(self):
        for produto in self.gerenciamento_produto.produtos:
            if produto.quantidade <= 15:
                print(f"{produto.nome} - Estoque baixo: {produto.quantidade} unidades")
            else:
                print("Nenhum produto com estoque baixo.")

    def menu_relatórios(self):
        while True:
            print("\n1. Relatório de Validade\n2. Relatório de Estoque Baixo\n0. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.relatorio_validade()
            elif opcao == "2":
                self.relatorio_estoque()
            elif opcao == "0":
                break
            else:
                print("** Opção inválida. **")