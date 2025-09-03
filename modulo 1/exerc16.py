"""
Exercício 16: Jogo de Adivinhação com Dicas
● Defina um número secreto.
● Use um while True e um contador de tentativas.
● A cada tentativa, diga se o palpite é "maior" ou "menor" que o número secreto.
● Quando o usuário acertar, imprima a mensagem de vitória e quantas tentativas foram
necessárias.


"""

numero_secreto = 42
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")
