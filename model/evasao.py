
# model/evasao.py
from model.aluno import Aluno

class Evasao:
    def __init__(self, id_evasao:int=None, data_evasao:str=None, motivo:str=None, ano_letivo:int=None, aluno:Aluno=None):
        self.id_evasao = id_evasao
        self.data_evasao = data_evasao
        self.motivo = motivo
        self.ano_letivo = ano_letivo
        self.aluno = aluno
    
    def to_string(self):
        return f"ID Evasão: {self.id_evasao}, Aluno: {self.aluno.nome_aluno if self.aluno else 'N/A'}, Motivo: {self.motivo}, Data: {self.data_evasao}"