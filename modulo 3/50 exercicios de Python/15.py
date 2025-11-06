import random

def remover_3_aleatorios(dicionario):
    try:
        chaves_para_remover = random.sample(list(dicionario.keys()), 3)
        print(f"Removendo: {chaves_para_remover}")
        for chave in chaves_para_remover:
            dicionario.pop(chave)
            
    except ValueError:
        print("Dicionário tem menos de 3 itens. Limpando tudo.")
        dicionario.clear()
        
    return dicionario

dic1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(f"Dic1 antes: {dic1}")
remover_3_aleatorios(dic1)
print(f"Dic1 depois: {dic1}\n")

dic2 = {'x': 10, 'y': 20}
print(f"Dic2 antes: {dic2}")
remover_3_aleatorios(dic2)
print(f"Dic2 depois: {dic2}")