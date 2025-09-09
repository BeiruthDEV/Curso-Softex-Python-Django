def maior_numero(lista):
    if not lista:
        return None
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

print(maior_numero([3, 7, 2, 9]))
