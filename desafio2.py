
ladoA = input("Digite o valor do lado A: ")
ladoB = input("Digite o valor do lado B: ")
ladoC = input("Digite o valor do lado C: ")


def eh_numero_positivo(valor):
    try:
        numero = float(valor)
        return numero > 0
    except ValueError:
        return False


if eh_numero_positivo(ladoA) and eh_numero_positivo(ladoB) and eh_numero_positivo(ladoC):
    ladoA = float(ladoA)
    ladoB = float(ladoB)
    ladoC = float(ladoC)

    
    if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
        if ladoA > abs(ladoB - ladoC) and ladoB > abs(ladoA - ladoC) and ladoC > abs(ladoA - ladoB):
            print("Os valores formam um triângulo!")
        else:
            print("Os valores não formam um triângulo.")
    else:
        print("Os valores não formam um triângulo.")
else:
    print("Por favor, insira números válidos e positivos.")
