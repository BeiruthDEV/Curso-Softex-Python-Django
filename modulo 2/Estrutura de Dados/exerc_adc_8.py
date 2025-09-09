"""
Conversão de Tipos: Crie uma lista cidades_lista = ['Paris', 'Londres', 'Tóquio']. Converta
essa lista para uma tupla. Depois, converta a tupla de volta para uma lista e adicione
'Nova York'.

"""


cidades_lista = ['Paris', 'Londres', 'Tóquio']


cidades_tupla = tuple(cidades_lista)
print("Tupla:", cidades_tupla)


cidades_lista = list(cidades_tupla)


cidades_lista.append('Nova York')
print("Lista final:", cidades_lista)
