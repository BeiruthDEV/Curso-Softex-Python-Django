tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada!")

def remover_tarefa():
    try:
        indice = int(input("Digite o índice da tarefa a remover: "))
        tarefa = tarefas.pop(indice)
        print(f"Tarefa '{tarefa}' removida!")
    except (ValueError, IndexError):
        print("Índice inválido!")

def listar_tarefas():
    if tarefas:
        for i, t in enumerate(tarefas):
            print(f"{i}: {t}")
    else:
        print("Nenhuma tarefa cadastrada.")

while True:
    print("\n1 - Adicionar Tarefa\n2 - Remover Tarefa\n3 - Listar Tarefas\n4 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        remover_tarefa()
    elif opcao == "3":
        listar_tarefas()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
