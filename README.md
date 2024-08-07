# Gerenciador de Tarefas com Tkinter

Este é um programa de gerenciamento de tarefas com interface gráfica desenvolvida em Python utilizando Tkinter. Ele permite adicionar, visualizar, marcar como concluídas e remover tarefas. As tarefas são salvas em um banco de dados SQLite3 para persistência de dados.

## Funcionalidades

1. **Menu de Opções**: Ao inicializar o programa, um menu de opções é exibido para o usuário escolher o que deseja fazer.
2. **Adicionar Tarefas**: Permite ao usuário adicionar uma nova tarefa com uma descrição.
3. **Visualizar Tarefas**: Exibe todas as tarefas, indicando quais estão concluídas e quais ainda estão pendentes.
4. **Marcar Tarefas como Concluídas**: Permite ao usuário marcar uma tarefa específica como concluída.
5. **Remover Tarefas**: Permite ao usuário remover uma tarefa específica da lista.
6. **Salvar e Carregar Tarefas**: Salva a lista de tarefas em um banco de dados SQLite3 para que possam ser carregadas na próxima execução do programa.
7. **Persistência de Dados**: Todos os dados inseridos ou modificados pelo usuário são armazenados no banco de dados SQLite3.
8. **Executável**: O programa pode ser convertido em um executável para que o usuário possa utilizá-lo sem a necessidade de instalar ferramentas adicionais.

## Requisitos

- Python 3.x
- Tkinter (geralmente incluído na instalação padrão do Python)
- SQLite3
