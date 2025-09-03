"""
Exercício 14: Somador de Números Positivos
● Use um while True para pedir números ao usuário.
● Some todos os números positivos.
● Se o usuário digitar um número negativo, use break para sair do loop e imprima a soma
total
"""

soma = 0
while True:
    num = float(input("Digite um número (negativo para sair): "))
    if num < 0:
        break
    soma += num
print(f"Soma total dos números positivos: {soma}")
