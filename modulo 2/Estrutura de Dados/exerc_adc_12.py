"""
Diferença de Conjuntos: Ainda com os conjuntos do exercício 10, use o método
.difference() para encontrar os clientes que são premium mas não são recentes.
"""

clientes_premium = {'Maria', 'Pedro', 'Ana'}
clientes_recentes = {'Ana', 'João', 'Lucas'}

premium_nao_recentes = clientes_premium.difference(clientes_recentes)

print(premium_nao_recentes)
