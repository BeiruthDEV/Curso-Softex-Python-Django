"""
Exercício 6: Verificador de Par ou Ímpar
● Peça ao usuário um número inteiro.
● Use o operador de módulo (%) e uma estrutura if-else para determinar e imprimir se o
número é "par" ou "ímpar"
"""

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
