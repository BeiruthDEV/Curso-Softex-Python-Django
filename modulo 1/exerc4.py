"""
Exercício 4: Verificador de Senha
● Defina uma senha secreta em uma variável (str, por exemplo, "python123").
● Peça ao usuário para digitar uma senha.
● Use if-else para verificar se a senha digitada é igual à senha secreta. Imprima "Acesso
concedido" ou "Senha incorreta"
"""

senha_secreta = "python123"
senha_digitada = input("Digite a senha: ")
if senha_digitada == senha_secreta:
    print("Acesso concedido")
else:
    print("Senha incorreta")
