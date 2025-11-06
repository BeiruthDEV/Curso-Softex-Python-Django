def fatiamento_circular(lista, inicio, fim):
    if fim >= inicio:
        return lista[inicio:fim]
    else:
        return lista[inicio:] + lista[:fim]

lista_circ = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(f"Lista completa: {lista_circ}")
print(f"Slice normal (2:5): {fatiamento_circular(lista_circ, 2, 5)}")
print(f"Slice circular (5:2): {fatiamento_circular(lista_circ, 5, 2)}")