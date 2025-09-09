"""
Registro de Acessos Únicos: Você tem uma lista de tuplas (usuario_id, page_id)
representando acessos de usuários a páginas. Crie um conjunto de tuplas para
armazenar todos os acessos únicos, removendo duplicações.
acessos = [(1, 'home'), (2, 'produtos'), (1, 'home'), (3, 'contato')]
"""

acessos = [(1, 'home'), (2, 'produtos'), (1, 'home'), (3, 'contato')]


acessos_unicos = set(acessos)

print(acessos_unicos)
