from caixa import Caixa
from produto import GerenciamentoProduto
from venda import GerenciamentoVenda
from relatorio import GeracaoRelatorio

def iniciar_sistema():
    caixa = Caixa()
    produtos = GerenciamentoProduto()
    vendas = GerenciamentoVenda(produtos, caixa)  # Passar o caixa para GerenciamentoVenda
    relatorios = GeracaoRelatorio(produtos)

    caixa.abrir_caixa()
    while True:
        print("-----------------------------------\nMenu Principal:")
        print("1. Cadastro de Produtos")
        print("2. Nova Venda")
        print("3. Relatórios")
        print("4. Fechar Caixa")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produtos.menu_produtos()
        elif opcao == "2":
            vendas.nova_venda()
        elif opcao == "3":
            relatorios.menu_relatórios()
        elif opcao == "4":
            if caixa.fechar_caixa() is False:
                continue  # Volta ao menu principal se o fechamento falhar
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()
