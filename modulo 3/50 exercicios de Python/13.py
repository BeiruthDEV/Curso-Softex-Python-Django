def gerar_metadados(dicionario):
    metadados = {}
    for chave, valor in dicionario.items():
        metadados[chave] = {
            'tipo': type(valor).__name__,
            'tamanho_chave': len(str(chave)),
            'é_par': (valor % 2 == 0) if isinstance(valor, int) else False
        }
    return metadados

dados_numericos = {'id_123': 42, 'valor_total': 105.5, 'codigo': 7}
import json
print(json.dumps(gerar_metadados(dados_numericos), indent=2))