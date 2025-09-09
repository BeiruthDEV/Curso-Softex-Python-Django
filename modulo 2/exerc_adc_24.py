inventario = {}

while True:
    print("\n1 - Adicionar item")
    print("2 - Listar itens")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do item: ").lower()
        dano = int(input("Dano do item: "))
        peso = float(input("Peso do item: "))
        inventario[nome] = {"dano": dano, "peso": peso}
        print(f"{nome} adicionado ao inventário!")

    elif opcao == "2":
        if inventario:
            for item, atributos in inventario.items():
                print(f"{item} -> Dano: {atributos['dano']}, Peso: {atributos['peso']}")
        else:
            print("Inventário vazio.")

    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
