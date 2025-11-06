def ordenar_por_valor(dicionario):
    lista_ordenada = sorted(dicionario.items(), key=lambda item: item[1], reverse=True)
    return lista_ordenada


pontuacoes = {'Ana': 85, 'Beto': 92, 'Carla': 78, 'Daniel': 95}
print(f"Ordenado por pontuação (decrescente): {ordenar_por_valor(pontuacoes)}")