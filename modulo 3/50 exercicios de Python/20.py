def chaves_para_maiusculas(dicionario):
    novo_dicionario = {str(chave).upper(): valor for chave, valor in dicionario.items()}
    return novo_dicionario

dados_mistos = {'nome': 'João', 'idade': 30, 'cidade_natal': 'Rio'}
print(f"Original: {dados_mistos}")
print(f"Chaves maiúsculas: {chaves_para_maiusculas(dados_mistos)}")