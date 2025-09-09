def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero não é permitida."

print(dividir(10, 2))
print(dividir(10, 0))
