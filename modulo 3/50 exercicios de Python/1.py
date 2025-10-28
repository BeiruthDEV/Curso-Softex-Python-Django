import random


def intersecao_listas():

    lista1 = [random.randint(1, 20) for _ in range(10)]
    lista2 = [random.randint(1, 20) for _ in range(10)]

    print("Lista 1:", lista1)
    print("Lista 2:", lista2)

    intersecao = list(set(lista1) & set(lista2))

    return intersecao


resultado = intersecao_listas()

print("Elementos em comum(sem repetição)", resultado)
