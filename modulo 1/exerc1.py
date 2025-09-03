"""
Exercício 1: Verificador de Positivo
● Peça ao usuário para digitar um número inteiro.
● Use uma estrutura if simples para verificar se o número é maior que zero.
● Se for, imprima "O número é positivo!"
"""

eh_positivo = int(input("Digite um número positivo:"))

if eh_positivo > 0:
    print("Numero Positivo")
else:
    print("Numero incorreto.")