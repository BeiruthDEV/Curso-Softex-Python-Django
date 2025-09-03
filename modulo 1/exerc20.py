"""
Exercício 20: Jogo da Forca Simplificado
● Defina uma palavra secreta em uma variável (str).
● Use um while para dar ao usuário 5 chances de adivinhar a palavra.
● A cada tentativa, o usuário digita uma letra.
● Se a letra estiver na palavra, exiba as letras já descobertas (ex: _ y t _ _ n).
● Se a letra não estiver, diminua as chances.
● Se o usuário acertar todas as letras, imprima a palavra completa e uma mensagem de
vitória. Se as chances acabarem, imprima a palavra e uma mensagem de derrota.
"""

palavra_secreta = "python"
chances = 5
letras_descobertas = ["_"] * len(palavra_secreta)

while chances > 0:
    print(" ".join(letras_descobertas))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_secreta:
        for i, char in enumerate(palavra_secreta):
            if char == letra:
                letras_descobertas[i] = letra
        if "_" not in letras_descobertas:
            print(" ".join(letras_descobertas))
            print("Parabéns! Você venceu!")
            break
    else:
        chances -= 1
        print(f"Letra não encontrada. Você tem {chances} chances restantes.")

if chances == 0:
    print(f"Você perdeu! A palavra era: {palavra_secreta}")
