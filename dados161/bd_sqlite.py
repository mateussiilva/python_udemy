import sqlite3 as sq 



#CRIA O ARQUIVO DA BASE DE DADOS 
conexao = sq.connect("basededados.db")


#RESPONSAVEL POR LER E INSERIR REGISTROS 
cursor = conexao.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS clientes ("
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'nome TEXT,'
        'peso REAL' ")"
) 


""" FORMA INSEGURA DE MANDAR DADOS DIRETAMENTE PRO BANCO DE DADOS """
# cursor.execute("INSERT INTO clientes (nome, peso) VALUES ('Mateus José',80.5)")


""" FORMA SEGURA E INTERESSANTE
    As interogações representam cada campo respectivamente
"""
#cursor.execute(
#    "INSERT INTO clientes VALUES (?,?,?)", (None,"Mateus José", 75.8)
#    )

# cursor.execute(
#     "INSERT INTO clientes VALUES (:id, :nome, :peso)",
#     {"id":None, "nome":"José", "peso": 54}
#     )

# ATUALIZANDO REGISTROS NA BASE DE DADOS

""" cursor.execute(
    "UPDATE clientes SET nome=:name WHERE id=:id",
    {"name": "Silva", "id":2}) """


# cursor.execute(
#     "DELETE FROM clientes WHERE id=:id",
#     {"id":2})

""" cursor.execute(
    "SELECT nome, peso FROM clientes WHERE peso > :peso",
    {"peso":15})
 """

conexao.commit()


# cursor.execute("SELECT * FROM clientes")

for line in cursor.fetchall():
    nome, peso = line
    print(nome, peso)
cursor.close()
conexao.close()
