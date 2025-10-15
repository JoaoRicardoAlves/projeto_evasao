# controller/controller_aluno.py
from conexion.db_connection import DBConnection
from model.aluno import Aluno
from controller.controller_escola import ControllerEscola

class ControllerAluno:
    def __init__(self, db_connection: DBConnection):
        self.db = db_connection
        self.ctrl_escola = ControllerEscola(db_connection)

    def get_aluno_by_id(self, id_aluno: int):
        query = "SELECT id_aluno, nome_aluno, data_nascimento, id_escola FROM aluno WHERE id_aluno = %s"
        result = self.db.execute_query(query, (id_aluno,))
        if result:
            row = result[0]
            escola = self.ctrl_escola.get_escola_by_id(row[3])
            return Aluno(id_aluno=row[0], nome_aluno=row[1], data_nascimento=str(row[2]), escola=escola)
        return None

    def get_all_alunos(self):
        query = "SELECT id_aluno, nome_aluno, id_escola FROM aluno ORDER BY nome_aluno"
        results = self.db.execute_query(query)
        alunos = []
        if results:
            for row in results:
                alunos.append(Aluno(id_aluno=row[0], nome_aluno=row[1], escola=Escola(id_escola=row[2])))
        return alunos

    def inserir_aluno(self, aluno: Aluno):
        query = "INSERT INTO aluno (nome_aluno, data_nascimento, id_escola) VALUES (%s, %s, %s)"
        params = (aluno.nome_aluno, aluno.data_nascimento, aluno.escola.id_escola)
        self.db.execute_query(query, params)
        print("Aluno inserido com sucesso!")

    def atualizar_aluno(self, aluno: Aluno):
        query = "UPDATE aluno SET nome_aluno = %s, data_nascimento = %s, id_escola = %s WHERE id_aluno = %s"
        params = (aluno.nome_aluno, aluno.data_nascimento, aluno.escola.id_escola, aluno.id_aluno)
        self.db.execute_query(query, params)
        print("Aluno atualizado com sucesso!")

    def remover_aluno(self, id_aluno: int):
        # Verifica se o aluno é FK na tabela evasao
        check_query = "SELECT COUNT(1) FROM evasao WHERE id_aluno = %s"
        result = self.db.execute_query(check_query, (id_aluno,))
        if result and result[0][0] > 0:
            print(f"Erro: O aluno com ID {id_aluno} não pode ser removido pois possui um registro de evasão.")
            return

        query = "DELETE FROM aluno WHERE id_aluno = %s"
        self.db.execute_query(query, (id_aluno,))
        print("Aluno removido com sucesso!")