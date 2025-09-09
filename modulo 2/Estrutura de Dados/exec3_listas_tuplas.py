"""
Você tem uma lista de tuplas, onde cada tupla é um registro de acesso (usuario, status_login).

O status_login pode ser 'sucesso' ou 'falha'.

Usando laços de repetição e condicionais, identifique e imprima:
1.  O nome dos usuários que tiveram pelo menos um login bem-sucedido.
2. O nome dos usuários que tiveram somente logins com falha.

O que vai entrar:
acessos = [("Pedro", "sucesso"), ("Ana", "falha"), ("Maria", "sucesso"), ("Pedro", "falha"),
("Ana", "falha")]

A saída esperada:

Usuários com pelo menos um login bem-sucedido:
{'Maria', 'Pedro'}

Usuários que tiveram somente logins com falha:
{'Ana'}
"""


acessos = [
    ("Pedro", "sucesso"),
    ("Ana","Falha"),
    ("Maria","sucesso"),
    ("Pedro","falha"),
    ("Ana","falha")
]


sucessos = set()
falhas = {}

for usuarios,status in acessos:
    if status == "sucesso":
        sucessos.add(usuarios)

    if usuarios not in falhas:
        falhas [usuarios] = True

    if status == "sucesso":
        falhas[usuarios] = False



somente_falha = {usuarios for usuarios, so_falha in falhas.items() if so_falha}

print("\nUsuarios com pelo menos um login:")
print(sucessos)

print("\n Usuarios que tiveram somente login com falha:")
print(somente_falha)