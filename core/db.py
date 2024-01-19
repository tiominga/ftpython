import sqlite3

# Conecta ao banco de dados SQLite (se não existir, ele será criado)
conexao = sqlite3.connect('dbftp.db')

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Cria uma tabela chamada 'usuarios' (se não existir)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
''')

# Insere dados na tabela 'usuarios'
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ('Alice', 25))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ('Bob', 30))

# Commit para salvar as alterações
conexao.commit()

# Seleciona todos os registros da tabela 'usuarios'
cursor.execute('SELECT * FROM usuarios')
registros = cursor.fetchall()

# Exibe os registros
print("Registros na tabela 'usuarios':")
for registro in registros:
    print(registro)

# Fecha a conexão
conexao.close()
