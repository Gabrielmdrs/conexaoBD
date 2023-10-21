import pyodbc

database = os.environ.get("DATABASE")
server = os.environ.get("SERVER")
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
port = os.environ.get("PORT")

#string de conexao
str_con = f'DRIVER={{SQL Server}};SERVER={server};PORT={port};\
        DATABASE={database};UID={user};PWD={password}'

#Conectar com BD
try:
    conexao = pyodbc.connect(str_con)
    cursor = conexao.cursor()
    print("Conectado com sucesso!")

except Exception as e:
    print(f'Erro ao conectar o BD{e}')

#Inserindo dados no BD (tabela alunos) (nome, )
sql = "INSERT INTO alunos (nome,ra,id_curso,semestre) VALUES (?,?,?,?)"
valores = ("JOSE","230018",1,2)
cursor.execute(sql,valores)
cursor.commit()

#Procurando dados no BD
sql_select = "SELECT * FROM alunos WHERE NOME = ?"
valor = "JOSE"
resultado = cursor.execute(sql_select, valor)
for linha in resultado.fetchall():
    print(linha)

#update na tabela




