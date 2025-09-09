tarefas = {}

quantidade = int(input("Quantas tarefas deseja adicionar? "))

for _ in range(quantidade):
    nome = input("Nome da tarefa: ")
    status = input("Status da tarefa (pendente, em andamento, concluído): ").lower()
    tarefas[nome] = status

print("\nTarefas pendentes:")
for nome, status in tarefas.items():
    if status == "pendente":
        print(f"- {nome}")
