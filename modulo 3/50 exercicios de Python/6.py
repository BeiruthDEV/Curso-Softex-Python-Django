def transpor_matriz(matriz):
    if not matriz:
        return []
    
    transposta = [[row[i] for row in matriz] for i in range(len(matriz[0]))]
    return transposta

matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print("Matriz Original:")
for linha in matriz_original:
    print(linha)

print("\nMatriz Transposta:")
for linha in transpor_matriz(matriz_original):
    print(linha)