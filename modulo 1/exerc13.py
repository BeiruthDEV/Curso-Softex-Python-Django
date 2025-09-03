"""
Exercício 13: Login com Tentativas
● Defina uma senha secreta.
● Use um while True e um contador de tentativas (máximo de 3).
● Se o usuário acertar a senha, imprima "Login bem-sucedido!" e use break.
● Se o usuário errar 3 vezes, imprima "Tentativas esgotadas!" e pare o programa.
"""

senha_secreta = "python123"
tentativas = 0

while True:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_secreta:
        print("Login bem-sucedido!")
        break
    tentativas += 1
    if tentativas == 3:
        print("Tentativas esgotadas!")
        break
