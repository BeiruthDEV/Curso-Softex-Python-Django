import random

def filtro_random(lista, n):
    try:
        return random.sample(lista, n)
    except ValueError:
        print(f"Erro: Não é possível selecionar {n} elementos únicos de uma lista com {len(lista)} itens.")
        lista_embaralhada = list(lista)
        random.shuffle(lista_embaralhada)
        return lista_embaralhada

minha_lista = range(1, 11) 
print(f"3 aleatórios: {filtro_random(minha_lista, 3)}")

print("Tentando pegar mais elementos do que existem:")
print(filtro_random(minha_lista, 15))