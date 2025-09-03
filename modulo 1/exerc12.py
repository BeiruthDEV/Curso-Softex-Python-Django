"""
Exercício 12: Acumulador de Soma
● Peça ao usuário para digitar 5 números.
● Use um while com um contador para somar todos os números digitados e imprimir o
resultado final
"""

soma = 0
contador = 0
while contador < 5:
    num = float(input("Digite um número: "))
    soma += num
    contador += 1
print(f"Soma total: {soma}")
