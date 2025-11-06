def achatar_dicionario(dicionario_aninhado, separador="_"):
    dicionario_achatado = {}
    for chave_pai, valor_pai in dicionario_aninhado.items():
        if isinstance(valor_pai, dict):
            for chave_filho, valor_filho in valor_pai.items():
                nova_chave = f"{chave_pai}{separador}{chave_filho}"
                dicionario_achatado[nova_chave] = valor_filho
        else:
            dicionario_achatado[chave_pai] = valor_pai
    return dicionario_achatado


config = {
    'usuario': {
        'nome': 'Alice',
        'tema': 'escuro'
    },
    'sistema': {
        'versao': 1.2,
        'ambiente': 'producao'
    },
    'ativo': True
}
print("Dicionário achatado:")
print(achatar_dicionario(config))