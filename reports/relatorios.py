# reports/relatorios.py
from conexion.db_connection import DBConnection
import os

class Relatorios:
    def __init__(self, db_connection: DBConnection):
        self.db = db_connection

    def _read_sql_file(self, file_path):
        try:
            # A codificação 'utf-8-sig' é mais robusta e remove caracteres invisíveis (BOM)
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                return f.read()
        except IOError as e:
            print(f"Erro ao ler o arquivo SQL {file_path}: {e}")
            return None

    def gerar_relatorio_evasao_detalhada(self):
        # Consulta SQL diretamente no código para garantir o funcionamento
        query = """
        SELECT
            a.nome_aluno,
            e.nome_escola,
            ev.data_evasao,
            ev.motivo,
            ev.ano_letivo
        FROM evasao ev
        JOIN aluno a ON ev.id_aluno = a.id_aluno
        JOIN escola e ON a.id_escola = e.id_escola
        ORDER BY e.nome_escola, a.nome_aluno;
        """
        
        resultados = self.db.execute_query(query)
        
        if resultados:
            print("\n-- Relatório de Evasão Detalhada --")
            print(f"{'Aluno':<30} | {'Escola':<30} | {'Data Evasão':<15} | {'Motivo':<30} | {'Ano Letivo':<10}")
            print("-" * 125)
            for row in resultados:
                print(f"{str(row[0]):<30} | {str(row[1]):<30} | {str(row[2]):<15} | {str(row[3]):<30} | {str(row[4]):<10}")
        else:
            print("Nenhum dado encontrado para o relatório.")

    def gerar_relatorio_evasao_por_motivo(self):
        # APLICANDO A MESMA CORREÇÃO PARA O RELATÓRIO 2
        query = """
        SELECT
            motivo,
            COUNT(id_evasao) AS total_evasoes
        FROM evasao
        GROUP BY motivo
        ORDER BY total_evasoes DESC;
        """
            
        resultados = self.db.execute_query(query)
        
        if resultados:
            print("\n-- Relatório de Evasões por Motivo --")
            print(f"{'Motivo':<40} | {'Total de Evasões':<20}")
            print("-" * 65)
            for row in resultados:
                print(f"{str(row[0]):<40} | {str(row[1]):<20}")
        else:
            print("Nenhum dado encontrado para o relatório.")