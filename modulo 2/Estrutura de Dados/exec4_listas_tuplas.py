"""
Você tem uma lista de tuplas (aluno, nota).

1. Identifique e imprima a maior nota alcançada.

2. Crie uma tupla com todos os alunos que tiraram a maior nota.

3. Crie um conjunto de todos os alunos que tiveram uma nota menor que 7.0.

O que vai entrar:
notas = [("Ana", 9.5), ("João", 8.0), ("Maria", 10.0), ("Pedro", 7.5), ("Ana", 10.0), ("Carlos", 6.5)]

A saída esperada:

A maior nota alcançada é: 10.0

Alunos que tiraram a maior nota: ('Maria', 'Ana')

Alunos que tiveram nota menor que 7.0: {'Carlos'}
"""
notas = [
    ("Ana", 9.5),
    ("João", 8.0),
    ("Maria", 10.0),
    ("Pedro", 7.5),
    ("Ana", 10.0),
    ("Carlos", 6.5)
]

maior_nota = max(nota for _, nota in notas)

print(f'A maior nota alcançada é {maior_nota}')

alunos_maior_nota = tuple(aluno for aluno,nota in notas if nota == maior_nota)

print(f'\nAlunos que tiveram a maior nota{alunos_maior_nota}')

alunos_nota_menor_que_7 = {aluno for aluno,nota in notas if nota < 7}

print(f'\nAlunos que tiveram nota menor que 7: {alunos_nota_menor_que_7}')


