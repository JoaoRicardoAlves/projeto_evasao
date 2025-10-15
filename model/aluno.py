# model/aluno.py
from model.escola import Escola

class Aluno:
    def __init__(self, id_aluno:int=None, nome_aluno:str=None, data_nascimento:str=None, escola:Escola=None):
        self.id_aluno = id_aluno
        self.nome_aluno = nome_aluno
        self.data_nascimento = data_nascimento
        self.escola = escola

    def to_string(self):
        return f"ID: {self.id_aluno}, Nome: {self.nome_aluno}, Nascimento: {self.data_nascimento}, ID Escola: {self.escola.id_escola if self.escola else 'N/A'}"