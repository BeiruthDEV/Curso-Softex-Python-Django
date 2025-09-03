"""
Exercício 9: Categoria de CNH
● Peça a idade e se o usuário tem CNH (True ou False).
● Use if-elif-else com operadores lógicos (and e or) para:
○ Se for maior de 18 e tiver CNH: "Pode dirigir."
○ Se for maior de 18 e não tiver CNH: "Precisa tirar a CNH."
○ Se for menor de 18: "Não pode dirigir.
"""

idade = int(input("Digite sua idade: "))
tem_cnh = input("Você tem CNH? (True/False): ") == "True"

if idade >= 18 and tem_cnh:
    print("Pode dirigir.")
elif idade >= 18 and not tem_cnh:
    print("Precisa tirar a CNH.")
else:
    print("Não pode dirigir.")
