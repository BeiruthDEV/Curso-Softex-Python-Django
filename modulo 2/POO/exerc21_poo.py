def solicitar_inteiro():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

numero = solicitar_inteiro()
print("Você digitou:", numero)
