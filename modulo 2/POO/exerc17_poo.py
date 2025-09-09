def combinador(nome, *args, **kwargs):
    print(f"Nome: {nome}")
    if args:
        print("Args:", args)
    if kwargs:
        print("Kwargs:")
        for chave, valor in kwargs.items():
            print(f"{chave}: {valor}")

combinador("Matheus", 25, "Engenheiro", cidade="Rio", pais="Brasil")
