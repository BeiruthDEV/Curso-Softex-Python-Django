"""
Exercício 5: Maior de Dois Números
● Peça ao usuário para digitar dois números inteiros.
● Use if-else para descobrir qual dos dois é o maior e imprima o resultado.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print(f"O maior número é {num1}")
else:
    print(f"O maior número é {num2}")
