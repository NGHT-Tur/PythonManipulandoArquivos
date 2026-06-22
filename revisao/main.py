import super_calculadora as calc
from analisador_colecoes import menu_classificar
import filtrar_estoque
from acesso.validar_acesso import menu_acesso
import relatorios

while True:
    opcao = int(input("\nEscolha:\n1 - Super Calculadora:\n2 - Analisador de coleções:\n3 - Filtro de estoque:\n4 - Validador de acesso:\n5 - Relatórios:\n0 - Para Sair:\n"))
    if opcao == 1:
        calc.menu_calculadora()
    elif opcao == 2:
        menu_classificar()
    elif opcao == 3:
        filtrar_estoque.menu_estoque()
    elif opcao == 4:
        menu_acesso()
    elif opcao == 5:
        relatorios.relatorio_teste()
    elif opcao == 0:
        break
    else:
        print("Opção Inválida!")
        