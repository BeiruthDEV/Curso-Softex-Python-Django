"""
. Verificando um Subconjunto: Crie dois conjuntos: pratos_veganos = {'salada', 'arroz',
'feijão'} e cardapio = {'pizza', 'salada', 'arroz', 'feijão'}. Verifique se pratos_veganos é um
subconjunto de cardapio.

"""

pratos_veganos = {'salada', 'arroz', 'feijão'}
cardapio = {'pizza', 'salada', 'arroz', 'feijão'}


if pratos_veganos.issubset(cardapio):
    print("Todos os pratos veganos estão no cardápio.")
else:
    print("Nem todos os pratos veganos estão no cardápio.")
