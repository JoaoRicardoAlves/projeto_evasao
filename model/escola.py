# model/escola.py
class Escola:
    def __init__(self, id_escola:int=None, nome_escola:str=None, cidade:str=None, estado:str=None, regiao:str=None):
        self.id_escola = id_escola
        self.nome_escola = nome_escola
        self.cidade = cidade
        self.estado = estado
        self.regiao = regiao

    def to_string(self):
        return f"ID: {self.id_escola}, Nome: {self.nome_escola}, Cidade: {self.cidade}, Estado: {self.estado}"