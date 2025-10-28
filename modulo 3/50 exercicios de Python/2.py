def rotacionar_lista(lista, k):

    k = k % len(lista)

    return lista[-k:] + lista[:-k]


lista = [1, 2, 3, 4, 5]

resultado = rotacionar_lista(lista, 2)

print("Lista original", lista)

print("Lista rotacionada", resultado)
