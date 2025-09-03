"""
Exercício 11: Tabuada Simples
● Peça um número ao usuário.
● Use um while para imprimir a tabuada desse número, de 1 a 10.
○ Exemplo: 5 x 1 = 5, 5 x 2 = 10, etc.

"""

num = int(input("Digite um número: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
