# utils/splash_screen.py
from conexion.db_connection import DBConnection
from datetime import datetime

class SplashScreen:
    def __init__(self, db_connection: DBConnection):
        self.db = db_connection

    def get_counts(self):
        counts = {
            "escolas": self.db.get_table_count('escola'),
            "alunos": self.db.get_table_count('aluno'),
            "evasoes": self.db.get_table_count('evasao')
        }
        return counts

    def display(self):
        counts = self.get_counts()
        print("############################################################")
        print("##                                                        ##")
        print("##      SISTEMA DE ANÁLISE DE EVASÃO ESCOLAR              ##")
        print("##                                                        ##")
        print("############################################################")
        print("\nTOTAL DE REGISTROS EXISTENTES:")
        print(f"1 - ESCOLAS: {counts['escolas']}")
        print(f"2 - ALUNOS: {counts['alunos']}")
        print(f"3 - EVASÕES: {counts['evasoes']}")
        print("\nCRIADO POR:")
        print("- JOAO RICARDO")
        print("\nDISCIPLINA: Banco de Dados")
        print(f"{datetime.now().year}/{'1' if datetime.now().month < 7 else '2'}")
        print("PROFESSOR: Howard Roatti")
        print("############################################################\n")