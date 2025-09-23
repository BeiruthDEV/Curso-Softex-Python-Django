"""
Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:

A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.

lA<lB+lC

lB<lA+lC

lC<lA+lB

A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.

lA>∣lB−lC∣

lB>∣lA−lC∣

lC>∣lA−lB∣

Dica: use o método abs() para ter o valor absoluto de um número.
"""

ladoA = input("Digite o valor do lado A: ")
ladoB = input("Digite o valor do lado B: ")
ladoC = input("Digite o valor do lado C: ")


def eh_numero_positivo(valor):
    try:
        numero = float(valor)
        return numero > 0
    except ValueError:
        return False


if (
    eh_numero_positivo(ladoA)
    and eh_numero_positivo(ladoB)
    and eh_numero_positivo(ladoC)
):
    ladoA = float(ladoA)
    ladoB = float(ladoB)
    ladoC = float(ladoC)

    if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
        if (
            ladoA > abs(ladoB - ladoC)
            and ladoB > abs(ladoA - ladoC)
            and ladoC > abs(ladoA - ladoB)
        ):
            print("Os valores formam um triângulo!")
        else:
            print("Os valores não formam um triângulo.")
    else:
        print("Os valores não formam um triângulo.")
else:
    print("Por favor, insira números válidos e positivos.")
