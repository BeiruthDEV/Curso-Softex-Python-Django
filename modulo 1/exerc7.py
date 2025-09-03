"""
Exercício 7: Classificador de Idade
● Peça a idade de uma pessoa.
● Use if-elif-else para classificar a idade em:
○ "Criança" (0 a 12 anos)
○ "Adolescente" (13 a 17 anos)
○ "Adulto" (18 a 59 anos)
○ "Idoso" (60 anos ou mais)

"""

idade = int(input("Digite a idade: "))
if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
else:
    print("Idoso")
