unidades = {"metros": 1, "quilômetros": 1000, "centímetros": 0.01, "milímetros": 0.001}

quantidade = float(input("Digite a quantidade: "))
origem = input(
    "Digite a unidade de origem (metros, quilômetros, centímetros, milímetros): "
).lower()
destino = input(
    "Digite a unidade de destino (metros, quilômetros, centímetros, milímetros): "
).lower()

if origem in unidades and destino in unidades:
    em_metros = quantidade * unidades[origem]
    convertido = em_metros / unidades[destino]
    print(f"{quantidade} {origem} equivalem a {convertido} {destino}")
else:
    print("Unidade inválida!")
