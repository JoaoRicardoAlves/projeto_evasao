#===================================================================
#Scripit que faz a inicialização do BD
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent

def iniciar_banco():
    script_path = ROOT / "start_docker_db.py"
    subprocess.run(["python", str(script_path)], check=True)
#===================================================================

# Chama a função de inicialização
iniciar_banco()
# principal.py
from conexion.db_connection import DBConnection
from utils.splash_screen import SplashScreen
from utils import config
from reports.relatorios import Relatorios
from popular_banco import popular_banco_de_dados

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

def verificar_e_popular_banco():
    """Verifica se o banco de dados está vazio e o popula se necessário."""
    total_escolas = db.get_table_count('escola')
    if total_escolas == 0:
        print("Banco de dados vazio. Iniciando o processo de povoamento com dados fictícios.")
        print("Isso pode levar alguns instantes...")
        print("========================================================================")
        popular_banco_de_dados(db)
        print("========================================================================")
        print("Povoamento do banco de dados concluído com sucesso!")
        input("Pressione Enter para iniciar a aplicação...")
    else:
        print("Banco de dados já populado. Iniciando aplicação...")


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
            if db.get_table_count('escola') == 0:
                print("\nERRO: Nenhuma escola cadastrada. Insira uma escola primeiro.")
                continue
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
            if db.get_table_count('aluno') == 0:
                print("\nERRO: Nenhum aluno cadastrado. Insira um aluno primeiro.")
                continue
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
        # Sai do loop de inserção após uma operação bem-sucedida
        break

def handle_atualizar():
    while True:
        entidade = config.menu_entidades("Atualizar")
        if entidade == '1': # Escola
            escolas = ctrl_escola.get_all_escolas()
            for e in escolas: print(e.to_string())
            try:
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
            except ValueError:
                print("ID inválido. Por favor, insira um número.")
        elif entidade == '2': # Aluno
            alunos = ctrl_aluno.get_all_alunos()
            for a in alunos: print(a.to_string())
            try:
                id_aluno = int(input("ID do aluno a ser atualizado: "))
                aluno_existente = ctrl_aluno.get_aluno_by_id(id_aluno)
                if aluno_existente:
                    nome = input(f"Novo nome ({aluno_existente.nome_aluno}): ") or aluno_existente.nome_aluno
                    dt_nasc = input(f"Nova data de nascimento ({aluno_existente.data_nascimento}): ") or aluno_existente.data_nascimento
                    
                    escolas = ctrl_escola.get_all_escolas()
                    for e in escolas: print(e.to_string())
                    id_escola = input(f"Novo ID da escola ({aluno_existente.escola.id_escola}): ")
                    
                    escola_nova = ctrl_escola.get_escola_by_id(int(id_escola)) if id_escola else aluno_existente.escola

                    if escola_nova:
                        aluno_atualizado = Aluno(id_aluno, nome, dt_nasc, escola_nova)
                        ctrl_aluno.atualizar_aluno(aluno_atualizado)
                    else:
                        print("Nova escola não encontrada.")
                else:
                    print("Aluno não encontrado.")
            except ValueError:
                print("ID inválido. Por favor, insira um número.")
        elif entidade == '3': # Evasão
            evasoes = ctrl_evasao.get_all_evasoes()
            for ev in evasoes: print(ev.to_string())
            try:
                id_evasao = int(input("ID do registro de evasão a ser atualizado: "))
                evasao_existente = ctrl_evasao.get_evasao_by_id(id_evasao) # Supondo que este método exista
                if evasao_existente:
                    motivo = input(f"Novo motivo ({evasao_existente.motivo}): ") or evasao_existente.motivo
                    data_evasao = input(f"Nova data ({evasao_existente.data_evasao}): ") or str(evasao_existente.data_evasao)
                    ano_letivo = input(f"Novo ano letivo ({evasao_existente.ano_letivo}): ") or evasao_existente.ano_letivo
                    
                    # A lógica para alterar o aluno associado pode ser complexa, vamos manter o mesmo.
                    evasao_atualizada = Evasao(id_evasao, data_evasao, motivo, int(ano_letivo), evasao_existente.aluno)
                    ctrl_evasao.atualizar_evasao(evasao_atualizada)
                else:
                    print("Registro de evasão não encontrado.")
            except ValueError:
                print("ID ou ano inválido. Por favor, insira um número.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
                print("Verifique se o método get_evasao_by_id existe no ControllerEvasao.")

        elif entidade == '4':
            break
        else:
            print("Opção inválida.")
        # Sai do loop de atualização após uma operação
        break

def handle_remover():
    while True:
        entidade = config.menu_entidades("Remover")
        if entidade == '1': # Escola
            escolas = ctrl_escola.get_all_escolas()
            if not escolas:
                print("Nenhuma escola para remover.")
                break
            for e in escolas: print(e.to_string())
            try:
                id_escola = int(input("ID da escola a ser removida: "))
                confirm = input(f"Tem certeza que deseja remover a escola ID {id_escola}? (S/N): ").upper()
                if confirm == 'S':
                    ctrl_escola.remover_escola(id_escola)
            except ValueError:
                print("ID inválido. Por favor, insira um número.")
        elif entidade == '2': # Aluno
            alunos = ctrl_aluno.get_all_alunos()
            if not alunos:
                print("Nenhum aluno para remover.")
                break
            for a in alunos: print(a.to_string())
            try:
                id_aluno = int(input("ID do aluno a ser removido: "))
                confirm = input(f"Tem certeza que deseja remover o aluno ID {id_aluno}? (S/N): ").upper()
                if confirm == 'S':
                    ctrl_aluno.remover_aluno(id_aluno)
            except ValueError:
                print("ID inválido. Por favor, insira um número.")
        elif entidade == '3': # Evasão
            evasoes = ctrl_evasao.get_all_evasoes()
            if not evasoes:
                print("Nenhum registro de evasão para remover.")
                break
            for ev in evasoes: print(ev.to_string())
            try:
                id_evasao = int(input("ID do registro de evasão a ser removido: "))
                confirm = input(f"Tem certeza que deseja remover a evasão ID {id_evasao}? (S/N): ").upper()
                if confirm == 'S':
                    ctrl_evasao.remover_evasao(id_evasao)
            except ValueError:
                print("ID inválido. Por favor, insira um número.")
        elif entidade == '4':
            break
        else:
            print("Opção inválida.")
        # Sai do loop de remoção após uma operação
        break

if __name__ == "__main__":
    verificar_e_popular_banco()
    run()