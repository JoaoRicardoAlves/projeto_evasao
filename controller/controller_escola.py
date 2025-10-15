# controller/controller_escola.py
from conexion.db_connection import DBConnection
from model.escola import Escola

class ControllerEscola:
    def __init__(self, db_connection: DBConnection):
        self.db = db_connection

    def get_escola_by_id(self, id_escola: int):
        query = "SELECT id_escola, nome_escola, cidade, estado, regiao FROM escola WHERE id_escola = %s"
        result = self.db.execute_query(query, (id_escola,))
        if result:
            row = result[0]
            return Escola(id_escola=row[0], nome_escola=row[1], cidade=row[2], estado=row[3], regiao=row[4])
        return None

    def get_all_escolas(self):
        query = "SELECT id_escola, nome_escola, cidade, estado FROM escola ORDER BY nome_escola"
        results = self.db.execute_query(query)
        escolas = []
        if results:
            for row in results:
                escolas.append(Escola(id_escola=row[0], nome_escola=row[1], cidade=row[2], estado=row[3]))
        return escolas

    def inserir_escola(self, escola: Escola):
        query = "INSERT INTO escola (nome_escola, cidade, estado, regiao) VALUES (%s, %s, %s, %s)"
        params = (escola.nome_escola, escola.cidade, escola.estado, escola.regiao)
        self.db.execute_query(query, params)
        print("Escola inserida com sucesso!")

    def atualizar_escola(self, escola: Escola):
        query = "UPDATE escola SET nome_escola = %s, cidade = %s, estado = %s, regiao = %s WHERE id_escola = %s"
        params = (escola.nome_escola, escola.cidade, escola.estado, escola.regiao, escola.id_escola)
        self.db.execute_query(query, params)
        print("Escola atualizada com sucesso!")

    def remover_escola(self, id_escola: int):
        # Verifica se a escola é FK na tabela aluno
        check_query = "SELECT COUNT(1) FROM aluno WHERE id_escola = %s"
        result = self.db.execute_query(check_query, (id_escola,))
        if result and result[0][0] > 0:
            print(f"Erro: A escola com ID {id_escola} não pode ser removida pois está associada a {result[0][0]} aluno(s).")
            return

        query = "DELETE FROM escola WHERE id_escola = %s"
        self.db.execute_query(query, (id_escola,))
        print("Escola removida com sucesso!")