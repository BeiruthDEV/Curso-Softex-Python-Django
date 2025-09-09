"""
. Análise de Dados de Vendas: Você tem uma lista de vendas, onde cada venda é uma
tupla (produto, valor).
vendas = [('teclado', 150), ('mouse', 80), ('teclado', 150)]
Calcule o valor total de vendas. Em seguida, use um conjunto para contar quantos tipos
de produtos diferentes foram vendidos.

"""


vendas = [('teclado', 150), ('mouse', 80), ('teclado', 150)]


total_vendas = sum(valor for _, valor in vendas)
print("Valor total de vendas:", total_vendas)


produtos_unicos = {produto for produto, _ in vendas}
print("Tipos diferentes de produtos vendidos:", len(produtos_unicos))
