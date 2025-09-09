"""
Você tem o inventário de uma loja em duas listas de tuplas. Cada tupla representa um produto
(nome_do_produto, id).
● estoque_principal: Produtos disponíveis na loja.
● estoque_online: Produtos disponíveis no site.

Usando conjuntos, descubra e imprima:
1. Os produtos que estão disponíveis tanto na loja física quanto no site.
2. Os produtos que estão apenas na loja física.
3. Os produtos que estão apenas no site.

O que vai entrar:
estoque_principal = [("Camiseta", 101), ("Calça", 102), ("Boné", 103), ("Tênis", 104)]
estoque_online = [("Boné", 103), ("Camisa Polo", 105), ("Calça", 102), ("Chinelo", 106)]

A saída esperada:
Produtos disponíveis na loja e no site:
{('Boné', 103), ('Calça', 102)}
Produtos disponíveis apenas na loja física:
{('Camiseta', 101), ('Tênis', 104)}
Produtos disponíveis apenas no site:
{('Camisa Polo', 105), ('Chinelo', 106)}
"""

estoque_principal = [
    ("Camiseta",101),
    ("Calça",102),
    ("Boné",103),
    ("Tenis",104)
]

estoque_online = [
    ("Boné",103),
    ("Camisa Polo",105),
    ("Calça",102),
    ("Chinelo",106)
]

set_principal = set(estoque_principal)
set_online = set(estoque_online)

em_ambos = set_principal & set_online
apenas_loja_fisica = set_principal - set_online
apenas_online = set_online - set_principal


print("\nProdutos disponiveis em ambos:")
print(em_ambos)
print("\nProdutos disponiveis apenas em loja física:")
print(apenas_loja_fisica)
print("\nProdutos apenas em loja online:")
print(apenas_online)
