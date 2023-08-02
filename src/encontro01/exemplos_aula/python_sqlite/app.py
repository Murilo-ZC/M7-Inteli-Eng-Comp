import sqlite3
# Função para criar a tabela no banco de dados, caso não exista
def criar_tabela():
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
# Função para inserir um novo usuário no banco de dados
def inserir_usuario(nome, email):
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()
# Função para listar todos os usuários do banco de dados
def listar_usuarios():
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios
if __name__ == '__main__':
    criar_tabela()
    while True:
        print("1 - Inserir usuário")
        print("2 - Listar usuários")
        print("3 - Sair")
        opcao = input("Digite a opção desejada:")
        if opcao == '1':
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            inserir_usuario(nome, email)
            print("Usuário inserido com sucesso!")
        elif opcao == '2':
            usuarios = listar_usuarios()
            print("Lista de Usuários:")
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}")
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")