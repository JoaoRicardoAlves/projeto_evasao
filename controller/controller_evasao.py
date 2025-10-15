# controller/controller_evasao.py
from conexion.db_connection import DBConnection
from model.evasao import Evasao
from controller.controller_aluno import ControllerAluno

class ControllerEvasao:
    def __init__(self, db_connection: DBConnection):
        self.db = db_connection
        self.ctrl_aluno = ControllerAluno(db_connection)
    
    def get_all_evasoes(self):
        query = "SELECT ev.id_evasao, ev.motivo, a.id_aluno, a.nome_aluno FROM evasao ev JOIN aluno a ON ev.id_aluno = a.id_aluno"
        results = self.db.execute_query(query)
        evasoes = []
        if results:
            for row in results:
                aluno = self.ctrl_aluno.get_aluno_by_id(row[2])
                evasoes.append(Evasao(id_evasao=row[0], motivo=row[1], aluno=aluno))
        return evasoes

    def inserir_evasao(self, evasao: Evasao):
        query = "INSERT INTO evasao (data_evasao, motivo, ano_letivo, id_aluno) VALUES (%s, %s, %s, %s)"
        params = (evasao.data_evasao, evasao.motivo, evasao.ano_letivo, evasao.aluno.id_aluno)
        self.db.execute_query(query, params)
        print("Registro de evasão inserido com sucesso!")

    def atualizar_evasao(self, evasao: Evasao):
        query = "UPDATE evasao SET data_evasao = %s, motivo = %s, ano_letivo = %s, id_aluno = %s WHERE id_evasao = %s"
        params = (evasao.data_evasao, evasao.motivo, evasao.ano_letivo, evasao.aluno.id_aluno, evasao.id_evasao)
        self.db.execute_query(query, params)
        print("Registro de evasão atualizado com sucesso!")
        
    def remover_evasao(self, id_evasao: int):
        # Evasão não é FK em nenhuma outra tabela, então a remoção é direta
        query = "DELETE FROM evasao WHERE id_evasao = %s"
        self.db.execute_query(query, (id_evasao,))
        print("Registro de evasão removido com sucesso!")