"""
. Encontrando Elementos Comuns em Múltiplas Listas: Crie três listas: lista1 = [1, 2, 3,
4], lista2 = [3, 4, 5, 6], lista3 = [4, 6, 7, 8]. Use conjuntos para encontrar o(s) número(s)
que aparece(m) nas três listas
"""


lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
lista3 = [4, 6, 7, 8]


conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)


comuns = conjunto1.intersection(conjunto2, conjunto3)

print(comuns)
