def inverter_filtrar(dicionario):
    dicionario_invertido = {
        valor: chave 
        for chave, valor in dicionario.items() 
        if isinstance(valor, str) and len(valor) > 5
    }
    return dicionario_invertido

dados = {'a': 'curto', 'b': 'string_longa', 'c': 100, 'd': 'outra_longa'}
print(f"Original: {dados}")
print(f"Invertido e filtrado: {inverter_filtrar(dados)}")