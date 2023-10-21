import os
from ssl import _PasswordType
import pyodbc


class DatabaseManager():
    def __init__(self):
        self.server = os.environ.get("SERVER")
        self.database = os.environ.get("DATABASE")
        self.user = os.environ.get("USER")
        self.password = os.environ.get("PASSWORD")
        self.port = os.environ.get("PORT")
        self.cursor = None
       
        
    def conectar(self):
        str_con = f'DRIVER={{SQL Server}};SERVER={self.server};PORT={self.port};\
        DATABASE={self.database};UID={self.user};PWD={_PasswordType}'
        
        try:
            conexao = pyodbc.connect(str_con)
            self.cursor = conexao.cursor()
            print("Conectado com sucesso!")

        except Exception as e:
            print(f'Erro ao conectar o BD{e}')
            
    def desconectar(self):
        pass