import sqlite3

try:
    conexao = sqlite3.connect('basedados.db')
    cursor = conexao.cursor()

    # cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
    #                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    #                'nome TEXT,'
    #                'peso REAL'
    #                ')')

    # cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
    # cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Joaozinho', 'peso': 25.6})
    # cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Daniel', 'peso': 113.96})
    # conexao.commit()

    # cursor.execute('update clientes set nome=:nome, peso=:peso where id=:id', {'nome': 'Fernando', 'peso': 97, 'id': 2})
    # conexao.commit()

    cursor.execute('select * from clientes')

    for linha in cursor.fetchall():
        ident, nome, peso = linha
        print(ident, nome, peso)

finally:
    cursor.close()
    conexao.close()

