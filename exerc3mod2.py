numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = []

for x in numeros:
    if x > 1:
        eh_primo = True
        for i in range(2, x):
            if x % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(x)

print(primos)  

#O código percorre uma lista de números, verifica para cada um se é maior que 1 e se não tem divisores além de 1 e ele mesmo, e adiciona os números que passam nesse teste em uma nova lista de primos, que é impressa no final.