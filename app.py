""" Importando as bilbiotecas """
import tkinter as tk
from tkinter import messagebox
import sqlite3


""" Criando uma função para criar uma tabela e conectar ao banco de dados sqlite3 """
def criar_tabela():
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tarefas
                 (id INTEGER PRIMARY KEY, descricao TEXT, concluida BOOLEAN)''')
    conn.commit()
    conn.close()

""" Criando a função para adicionar a tarefa"""
def adicionar_tarefa():
    descricao = entry_descricao.get()
    if descricao:
        conn = sqlite3.connect('tarefas.db')
        c = conn.cursor()
        c.execute("INSERT INTO tarefas (descricao, concluida) VALUES (?, ?)", (descricao, False))
        conn.commit()
        conn.close()
        entry_descricao.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
    else:
        messagebox.showwarning("Aviso", "A descrição da tarefa não pode estar vazia.")

""" Criando a função para visualizar a tarefa """
def visualizar_tarefas():
    conn = sqlite3.connect('tarefas.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tarefas")
    tarefas = c.fetchall()
    conn.close()
    tarefas_text.delete(1.0, tk.END)
    for tarefa in tarefas:
        status = "Concluída" if tarefa[2] else "Pendente"
        tarefas_text.insert(tk.END, f"{tarefa[0]}. {tarefa[1]} - {status}\n")

""" Criando a função para marcar a tarefa como concluída """
def marcar_tarefa_concluida():
    id_tarefa = entry_id.get()
    if id_tarefa:
        conn = sqlite3.connect('tarefas.db')
        c = conn.cursor()
        c.execute("UPDATE tarefas SET concluida = ? WHERE id = ?", (True, id_tarefa))
        conn.commit()
        conn.close()
        entry_id.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Tarefa marcada como concluída!")
        messagebox.showwarning("Aviso", "O ID da tarefa não pode estar vazio.")

""" Criando a função para remover a tarefa"""
def remover_tarefa():
    id_tarefa = entry_id.get()
    if id_tarefa:
        conn = sqlite3.connect('tarefas.db')
        c = conn.cursor()
        c.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
        conn.commit()
        conn.close()
        entry_id.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Tarefa removida com sucesso!")
    else:
        messagebox.showwarning("Aviso", "O ID da tarefa não pode estar vazio.")

""" Criando a função para criar o menu do programa usando o tkinter"""
def main():
    criar_tabela()
    root = tk.Tk()
    root.title("Gerenciador de Tarefas")

    global entry_descricao, entry_id, tarefas_text

    tk.Label(root, text="Descrição da Tarefa:").pack()
    entry_descricao = tk.Entry(root)
    entry_descricao.pack()

    tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa).pack()

    tk.Label(root, text="ID da Tarefa:").pack()
    entry_id = tk.Entry(root)
    entry_id.pack()

    tk.Button(root, text="Marcar Tarefa como Concluída", command=marcar_tarefa_concluida).pack()
    tk.Button(root, text="Remover Tarefa", command=remover_tarefa).pack()

    tk.Button(root, text="Visualizar Tarefas", command=visualizar_tarefas).pack()

    tarefas_text = tk.Text(root, height=10, width=50)
    tarefas_text.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
