"""
Nível 1: Fundamentos
Neste nível, você vai praticar a manipulação básica de listas, loops e condições simples.
Exercício 1: Contando Ocorrências
Crie um programa que conte quantas vezes um número específico aparece em uma lista.
● Entrada: Uma lista de números e um número para ser procurado.
● Saída: Um número inteiro que representa a quantidade de vezes que o número
procurado aparece na lista.
Exemplo:
numeros = [1, 5, 2, 8, 5, 3, 5]
numero_procurado = 5
Resultado Esperado:
3
"""

numeros = [1, 5, 2, 8, 5, 3, 5]
numero_procurado = 5

quantidade_repeticoes = numeros.count(numero_procurado)

print(f"O numero se repete {quantidade_repeticoes} vezes")
