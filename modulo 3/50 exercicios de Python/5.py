def encontrar_duplicatas(lista):
    contagem = {}
    for item in lista:
        contagem[item] = contagem.get(item, 0) + 1
    
    duplicatas = [(item, freq) for item, freq in contagem.items() if freq > 1]
    return duplicatas


lista_teste = [1, 2, 3, 2, 4, 5, 1, 1, 6, 'a', 'b', 'a']
print(f"Duplicatas encontradas: {encontrar_duplicatas(lista_teste)}")