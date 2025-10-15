# conexion/db_connection.py
import psycopg2
from psycopg2 import sql

class DBConnection:
    def __init__(self, db_name, user, password, host='localhost', port='5432'):
        self.connection_params = {
            "dbname": db_name,
            "user": user,
            "password": password,
            "host": host,
            "port": port,
            "client_encoding": "latin1"
        }
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(**self.connection_params)
        except psycopg2.OperationalError as e:
            print(f"Erro ao conectar ao PostgreSQL: {e}")
            self.conn = None
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        conn = self.connect()
        if conn is None:
            return None
        
        with conn.cursor() as cur:
            try:
                cur.execute(query, params)
                if query.strip().upper().startswith("SELECT"):
                    return cur.fetchall()
            except psycopg2.Error as e:
                print(f"Erro na consulta: {e}")
                return None
            finally:
                conn.commit()
                self.close()
    
    def get_table_count(self, table_name):
        conn = self.connect()
        if conn is None:
            return 0
            
        with conn.cursor() as cur:
            try:
                query = sql.SQL("SELECT COUNT(1) FROM {}").format(sql.Identifier(table_name))
                cur.execute(query)
                count = cur.fetchone()[0]
                return count
            except psycopg2.Error as e:
                print(f"Não foi possível contar os registros da tabela {table_name}: {e}")
                return 0
            finally:
                self.close()