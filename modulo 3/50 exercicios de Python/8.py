def somar_listas(lista1, lista2):
    tamanho_max = max(len(lista1), len(lista2))
    soma_lista = []
    
    for i in range(tamanho_max):
        try:
            valor1 = lista1[i]
        except IndexError:
            valor1 = 0 
            
        try:
            valor2 = lista2[i]
        except IndexError:
            valor2 = 0 
            
        soma_lista.append(valor1 + valor2)
        
    return soma_lista


l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
print(f"Soma das listas: {somar_listas(l1, l2)}")