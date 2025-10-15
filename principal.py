# principal.py

# Importações de Módulos
from conexion.db_connection import DBConnection
from utils.splash_screen import SplashScreen
from utils import config
from reports.relatorios import Relatorios

# Importações de Controllers
from controller.controller_escola import ControllerEscola
from controller.controller_aluno import ControllerAluno
from controller.controller_evasao import ControllerEvasao

# Importações de Models
from model.escola import Escola
from model.aluno import Aluno
from model.evasao import Evasao

# Instancia a conexão com o banco de dados
# ATENÇÃO: Substitua com suas credenciais do PostgreSQL
db = DBConnection(db_name="evasao", user="consulta", password="teste123")

# Instancia os controllers
ctrl_escola = ControllerEscola(db)
ctrl_aluno = ControllerAluno(db)
ctrl_evasao = ControllerEvasao(db)
relatorios = Relatorios(db)

def run():
    config.clear_console()
    splash = SplashScreen(db)
    splash.display()

    while True:
        opcao = config.menu_principal()

        if opcao == '1': # Relatórios
            while True:
                rel_opcao = config.menu_relatorios()
                if rel_opcao == '1':
                    relatorios.gerar_relatorio_evasao_detalhada()
                elif rel_opcao == '2':
                    relatorios.gerar_relatorio_evasao_por_motivo()
                elif rel_opcao == '3':
                    break
                else:
                    print("Opção inválida.")
                input("\nPressione Enter para continuar...")

        elif opcao == '2': # Inserir
            handle_inserir()
        
        elif opcao == '3': # Atualizar
            handle_atualizar()

        elif opcao == '4': # Remover
            handle_remover()

        elif opcao == '5': # Sair
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        input("\nPressione Enter para continuar...")
        config.clear_console()
        splash.display()

def handle_inserir():
    while True:
        entidade = config.menu_entidades("Inserir")
        if entidade == '1': # Escola
            nome = input("Nome da escola: ")
            cidade = input("Cidade: ")
            estado = input("Estado (UF): ")
            regiao = input("Região: ")
            nova_escola = Escola(nome_escola=nome, cidade=cidade, estado=estado, regiao=regiao)
            ctrl_escola.inserir_escola(nova_escola)
        elif entidade == '2': # Aluno
            nome = input("Nome do aluno: ")
            dt_nasc = input("Data de Nascimento (YYYY-MM-DD): ")
            
            escolas = ctrl_escola.get_all_escolas()
            for e in escolas: print(e.to_string())
            id_escola = int(input("ID da escola do aluno: "))
            escola = ctrl_escola.get_escola_by_id(id_escola)
            if escola:
                novo_aluno = Aluno(nome_aluno=nome, data_nascimento=dt_nasc, escola=escola)
                ctrl_aluno.inserir_aluno(novo_aluno)
            else:
                print("Escola não encontrada.")
        elif entidade == '3': # Evasão
            motivo = input("Motivo da evasão: ")
            data_evasao = input("Data da evasão (YYYY-MM-DD): ")
            ano_letivo = int(input("Ano letivo da evasão: "))
            
            alunos = ctrl_aluno.get_all_alunos()
            for a in alunos: print(a.to_string())
            id_aluno = int(input("ID do aluno que evadiu: "))
            aluno = ctrl_aluno.get_aluno_by_id(id_aluno)
            if aluno:
                nova_evasao = Evasao(motivo=motivo, data_evasao=data_evasao, ano_letivo=ano_letivo, aluno=aluno)
                ctrl_evasao.inserir_evasao(nova_evasao)
            else:
                print("Aluno não encontrado.")
        elif entidade == '4':
            break
        else:
            print("Opção inválida.")

def handle_atualizar():
    while True:
        entidade = config.menu_entidades("Atualizar")
        if entidade == '1': # Escola
            escolas = ctrl_escola.get_all_escolas()
            for e in escolas: print(e.to_string())
            id_escola = int(input("ID da escola a ser atualizada: "))
            escola_existente = ctrl_escola.get_escola_by_id(id_escola)
            if escola_existente:
                nome = input(f"Novo nome ({escola_existente.nome_escola}): ") or escola_existente.nome_escola
                cidade = input(f"Nova cidade ({escola_existente.cidade}): ") or escola_existente.cidade
                estado = input(f"Novo estado ({escola_existente.estado}): ") or escola_existente.estado
                regiao = input(f"Nova região ({escola_existente.regiao}): ") or escola_existente.regiao
                escola_atualizada = Escola(id_escola, nome, cidade, estado, regiao)
                ctrl_escola.atualizar_escola(escola_atualizada)
            else:
                print("Escola não encontrada.")
        # Adicionar lógica para Aluno e Evasão similarmente...
        elif entidade == '4':
            break
        else:
            print("Opção inválida.")

def handle_remover():
    while True:
        entidade = config.menu_entidades("Remover")
        if entidade == '1': # Escola
            escolas = ctrl_escola.get_all_escolas()
            for e in escolas: print(e.to_string())
            id_escola = int(input("ID da escola a ser removida: "))
            confirm = input(f"Tem certeza que deseja remover a escola ID {id_escola}? (S/N): ").upper()
            if confirm == 'S':
                ctrl_escola.remover_escola(id_escola)
        elif entidade == '2': # Aluno
            alunos = ctrl_aluno.get_all_alunos()
            for a in alunos: print(a.to_string())
            id_aluno = int(input("ID do aluno a ser removido: "))
            confirm = input(f"Tem certeza que deseja remover o aluno ID {id_aluno}? (S/N): ").upper()
            if confirm == 'S':
                ctrl_aluno.remover_aluno(id_aluno)
        elif entidade == '3': # Evasão
            evasoes = ctrl_evasao.get_all_evasoes()
            for ev in evasoes: print(ev.to_string())
            id_evasao = int(input("ID do registro de evasão a ser removido: "))
            confirm = input(f"Tem certeza que deseja remover a evasão ID {id_evasao}? (S/N): ").upper()
            if confirm == 'S':
                ctrl_evasao.remover_evasao(id_evasao)
        elif entidade == '4':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    run()