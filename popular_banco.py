# popular_banco.py

# Importações necessárias
import random, sys
from faker import Faker # type: ignore

# Importações do seu projeto
from conexion.db_connection import DBConnection # type: ignore
from controller.controller_escola import ControllerEscola
from controller.controller_aluno import ControllerAluno
from controller.controller_evasao import ControllerEvasao
from model.escola import Escola
from model.aluno import Aluno
from model.evasao import Evasao

# ====================================================================
# CONFIGURAÇÕES
# ====================================================================
# Altere a quantidade de dados que deseja gerar
NUM_ESCOLAS = 50
NUM_ALUNOS = 1000
PERCENTUAL_EVASAO = 0.15  # 15% dos alunos irão evadir

# Inicializa o Faker para gerar dados em português do Brasil
faker = Faker('pt_BR')

def popular_escolas(db: DBConnection, ctrl_escola: ControllerEscola):
    """Gera e insere escolas no banco de dados."""
    print(f"Inserindo {NUM_ESCOLAS} escolas. Aguarde...")
    regioes = ["Sudeste", "Sul", "Nordeste", "Norte", "Centro-Oeste"]
    
    for i in range(NUM_ESCOLAS):
        nome = f"Escola Estadual {faker.last_name()} {faker.last_name()}"
        cidade = faker.city()
        estado = faker.state_abbr()
        regiao = random.choice(regioes)
        
        nova_escola = Escola(nome_escola=nome, cidade=cidade, estado=estado, regiao=regiao)
        ctrl_escola.inserir_escola(nova_escola)
        
        # Exibe progresso a cada 10 inserções
        if (i + 1) % 10 == 0:
            sys.stdout.write(f"\r  {i + 1}/{NUM_ESCOLAS} escolas inseridas...")
            sys.stdout.flush()

    print("\n✔ Escolas populadas com sucesso!")

def popular_alunos(db: DBConnection, ctrl_aluno: ControllerAluno):
    """Gera e insere alunos, associando-os a escolas existentes."""
    print(f"\nInserindo {NUM_ALUNOS} alunos. Isso pode levar um momento...")
    
    # Busca os IDs de todas as escolas já inseridas para garantir a integridade referencial
    escolas_result = db.execute_query("SELECT id_escola FROM escola")
    if not escolas_result:
        print("ERRO: Nenhuma escola encontrada no banco. Execute a população de escolas primeiro.")
        return
        
    escola_ids = [item[0] for item in escolas_result]

    for i in range(NUM_ALUNOS):
        nome = faker.name()
        # Gera data de nascimento para alunos do ensino médio (15 a 18 anos)
        data_nascimento = faker.date_of_birth(minimum_age=15, maximum_age=18)
        
        # Seleciona uma escola aleatória para o aluno
        id_escola_aleatoria = random.choice(escola_ids)
        # O controller espera um objeto Escola, mesmo que seja só com o ID
        escola_ref = Escola(id_escola=id_escola_aleatoria)
        
        novo_aluno = Aluno(nome_aluno=nome, data_nascimento=data_nascimento, escola=escola_ref)
        ctrl_aluno.inserir_aluno(novo_aluno)
        
        # Exibe progresso a cada 100 inserções
        if (i + 1) % 100 == 0:
            sys.stdout.write(f"\r  {i + 1}/{NUM_ALUNOS} alunos inseridos...")
            sys.stdout.flush()

    print("\n✔ Alunos populados com sucesso!")

def popular_evasoes(db: DBConnection, ctrl_evasao: ControllerEvasao):
    """Gera e insere registros de evasão para um percentual de alunos."""
    print(f"\nGerando registros de evasão para {PERCENTUAL_EVASAO:.0%} dos alunos...")
    
    # Motivos comuns para evasão escolar
    motivos = [
        "Necessidade de trabalhar", "Falta de interesse nos estudos", 
        "Dificuldades de aprendizado", "Problemas familiares", 
        "Mudança de cidade/estado", "Gravidez na adolescência", "Bullying"
    ]

    # Busca os IDs de todos os alunos
    alunos_result = db.execute_query("SELECT id_aluno FROM aluno")
    if not alunos_result:
        print("ERRO: Nenhum aluno encontrado no banco.")
        return
        
    aluno_ids = [item[0] for item in alunos_result]
    
    # Calcula quantos alunos irão evadir e seleciona uma amostra aleatória (sem repetição)
    num_evasoes = int(len(aluno_ids) * PERCENTUAL_EVASAO)
    ids_dos_evadidos = random.sample(aluno_ids, num_evasoes)

    for i, aluno_id in enumerate(ids_dos_evadidos):
        data_evasao = faker.date_between(start_date='-3y', end_date='today')
        motivo = random.choice(motivos)
        ano_letivo = data_evasao.year
        
        # O controller espera um objeto Aluno
        aluno_ref = Aluno(id_aluno=aluno_id)
        
        nova_evasao = Evasao(data_evasao=data_evasao, motivo=motivo, ano_letivo=ano_letivo, aluno=aluno_ref)
        ctrl_evasao.inserir_evasao(nova_evasao)
        
        if (i + 1) % 50 == 0:
            sys.stdout.write(f"\r  {i + 1}/{num_evasoes} registros de evasão inseridos...")
            sys.stdout.flush()
            
    print("\n✔ Registros de evasão populados com sucesso!")

def popular_banco_de_dados(db: DBConnection):
    """Executa a rotina completa de povoamento do banco de dados."""
    ctrl_escola = ControllerEscola(db)
    ctrl_aluno = ControllerAluno(db)
    ctrl_evasao = ControllerEvasao(db)

    # A ordem é importante por causa das chaves estrangeiras!
    popular_escolas(db, ctrl_escola)
    popular_alunos(db, ctrl_aluno)
    popular_evasoes(db, ctrl_evasao)

if __name__ == "__main__":
    # ATENÇÃO: Configure suas credenciais do banco de dados aqui para execução direta
    db_connection = DBConnection(db_name="evasao", user="consulta", password="teste123")

    print("==============================================")
    print("== INICIANDO SCRIPT DE POPULAÇÃO DO BANCO   ==")
    print("==============================================")
    popular_banco_de_dados(db_connection)
    print("\n==============================================")
    print("==         PROCESSO FINALIZADO            ==")
    print("==============================================")