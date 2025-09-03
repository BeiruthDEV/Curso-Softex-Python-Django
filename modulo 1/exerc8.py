"""
Exercício 8: Avaliador de Notas
● Peça a nota de um aluno (float).
● Use if-elif-else para atribuir um conceito:
○ = 9.0: Conceito A
○ = 7.0: Conceito B
○ = 5.0: Conceito C
○ < 5.0: Conceito D
"""

nota = float(input("Digite a nota do aluno: "))
if nota == 9.0:
    print("Conceito A")
elif nota == 7.0:
    print("Conceito B")
elif nota == 5.0:
    print("Conceito C")
elif nota < 5.0:
    print("Conceito D")
else:
    print("Nota sem conceito definido")
