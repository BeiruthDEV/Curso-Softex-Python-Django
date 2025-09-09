
agenda = {}

while True:
    print("\n--- MENU AGENDA ---")
    print("1 - Adicionar contato")
    print("2 - Consultar contato")
    print("3 - Listar todos os contatos")
    print("4 - Remover contato")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        agenda[nome] = telefone
        print(f"Contato {nome} adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome a consultar: ")
        if nome in agenda:
            print(f"{nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        if agenda:
            print("\n--- Lista de Contatos ---")
            for nome, telefone in agenda.items():
                print(f"{nome}: {telefone}")
        else:
            print("Agenda vazia.")

    elif opcao == "4":
        nome = input("Digite o nome do contato a remover: ")
        if nome in agenda:
            del agenda[nome]
            print(f"Contato {nome} removido com sucesso!")
        else:
            print("Contato não encontrado.")

    elif opcao == "5":
        print("Saindo da agenda. Até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")
