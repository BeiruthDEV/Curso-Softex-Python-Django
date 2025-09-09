"""
Interseção de Conjuntos: Usando os mesmos conjuntos do exercício anterior, use o
método .intersection() para encontrar os clientes que são tanto premium quanto
recentes.

"""


clientes_premium = {'Maria', 'Pedro', 'Ana'}
clientes_recentes = {'Ana', 'João', 'Lucas'}


clientes_comuns = clientes_premium.intersection(clientes_recentes)

print(clientes_comuns)
