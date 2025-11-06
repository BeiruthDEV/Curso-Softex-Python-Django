def maior_sequencia_contigua(lista):
    if not lista:
        return 0
        
    max_atual = lista[0]
    max_global = lista[0]
    
    for x in lista[1:]:
        max_atual = max(x, max_atual + x)
        
        if max_atual > max_global:
            max_global = max_atual
            
    return max_global

lista_numeros = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Lista: {lista_numeros}")
print(f"Soma máxima contígua: {maior_sequencia_contigua(lista_numeros)}")