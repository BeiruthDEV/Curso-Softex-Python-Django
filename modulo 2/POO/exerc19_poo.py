def ordenar_por_idade(lista):
    return sorted(lista, key=lambda x: x["idade"])

pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 20},
    {"nome": "Carlos", "idade": 30}
]

print(ordenar_por_idade(pessoas))
