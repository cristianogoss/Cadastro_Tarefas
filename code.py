import sqlite3

def criar_tabela():
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tarefas
                 (id INTEGER PRIMARY KEY, descricao TEXT, concluida BOOLEAN)''')
    conn.commit()
    conn.close()

def menu():
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()
    c.execute("INSERT INTO tarefas (descricao, concluida) VALUES (?, ?)", (descricao, False))
    conn.commit()
    conn.close()
    print("Tarefa adicionada com sucesso!")

def visualizar_tarefas():
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tarefas")
    tarefas = c.fetchall()
    conn.close()
    for tarefa in tarefas:
        status = "Concluída" if tarefa[2] else "Pendente"
        print(f"{tarefa[0]}. {tarefa[1]} - {status}")

def marcar_tarefa_concluida():
    id_tarefa = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()
    c.execute("UPDATE tarefas SET concluida = ? WHERE id = ?", (True, id_tarefa))
    conn.commit()
    conn.close()
    print("Tarefa marcada como concluída!")

def remover_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa a ser removida: "))
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()
    c.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    print("Tarefa removida com sucesso!")

def main():
    criar_tabela()
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            visualizar_tarefas()
        elif escolha == '3':
            marcar_tarefa_concluida()
        elif escolha == '4':
            remover_tarefa()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
