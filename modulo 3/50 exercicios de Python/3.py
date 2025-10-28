def remover_com_a(lista):
    i = 0
    while i < len(lista):
        if "a" in lista[i].lower():
            lista.pop(i)

        else:
            i += 1

    return lista


strings = ["Casa", "Bolo", "Amigo", "Sol", "Lua"]

resultado = remover_com_a(strings)

print(resultado)
