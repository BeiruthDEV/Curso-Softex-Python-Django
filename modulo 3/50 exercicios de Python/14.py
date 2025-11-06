def soma_condicional(dicionario, letra_inicio):
    soma_total = 0
    for chave, valor in dicionario.items():
        if chave.startswith(letra_inicio):
            try:
                soma_total += valor
            except TypeError:
                print(f"Aviso: Valor '{valor}' para a chave '{chave}' não é numérico. Ignorado.")
                
    return soma_total


produtos = {
    'papel': 10, 
    'caneta_azul': 2.5, 
    'caneta_vermelha': 'indisponível', 
    'caderno': 15,
    'pasta': 5
}
total_c = soma_condicional(produtos, 'c')
print(f"Soma dos itens com 'c': {total_c}")