"""
Exercício 2: Calculadora de Desconto
● Peça ao usuário para digitar o preço original de um produto (float).
● Se o preço for maior que R$ 100,00, aplique um desconto de 10% e imprima o novo
preço.
● Use o operador de multiplicação (*) e subtração (-)
"""

preco = float(input("Digite o preço do produto: "))
if preco > 100:
    preco = preco - (preco * 0.10)
print(f"Preço final: R$ {preco:.2f}")
