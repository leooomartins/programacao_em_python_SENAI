import sqlite3

conn  = sqlite3.connect('timaoeo.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS dados(
                
                nome TEXT,
                email TEXT,
                idade text,
                endereco TEXT,
                TRABALHO TEXT,
                GRADUACAO TEXT
               )''')
conn.commit()

nome  =  input('nome: ')
idade  =  input('idade: ')
email = input('e-mail:')
endereco = input('endereço:')
trabalho = input('trabalho:')
graduacao = input('graduação:')

cursor.execute('INSERT INTO dados VALUES(?,?,?,?,?,?)', (nome, email, idade, endereco, trabalho, graduacao))
conn.commit()

cursor.execute('SELECT * FROM dados')
dados  =  cursor.fetchall()
print(dados[0][0])

conn.close()