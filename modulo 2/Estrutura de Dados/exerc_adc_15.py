"""
 Comparação de Inventário: Você tem uma tupla de itens do seu estoque estoque =
('camisa', 'calça', 'sapato') e uma lista de itens que foram vendidos vendidos = ['camisa',
'meia', 'calça']. Use conjuntos para encontrar os itens que foram vendidos mas ainda
estão no estoque.

"""


estoque = ('camisa', 'calça', 'sapato')
vendidos = ['camisa', 'meia', 'calça']


estoque_set = set(estoque)
vendidos_set = set(vendidos)


vendidos_em_estoque = estoque_set.intersection(vendidos_set)

print(vendidos_em_estoque)
