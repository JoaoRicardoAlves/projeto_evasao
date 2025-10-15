# utils/config.py
def clear_console():
    # Comando para limpar o console (funciona em Linux, macOS e Windows)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    print("\n-- MENU PRINCIPAL --")
    print("1 - Relatórios")
    print("2 - Inserir Registros")
    print("3 - Atualizar Registros")
    print("4 - Remover Registros")
    print("5 - Sair")
    return input("Escolha uma opção: ")

def menu_entidades(operacao:str):
    print(f"\n-- {operacao.upper()} REGISTROS --")
    print("1 - Escola")
    print("2 - Aluno")
    print("3 - Evasão Escolar")
    print("4 - Voltar ao Menu Principal")
    return input("Escolha uma entidade: ")

def menu_relatorios():
    print("\n-- MENU DE RELATÓRIOS --")
    print("1 - Evasão Detalhada (Alunos e Escolas)")
    print("2 - Total de Evasões por Motivo")
    print("3 - Voltar ao Menu Principal")
    return input("Escolha um relatório: ")