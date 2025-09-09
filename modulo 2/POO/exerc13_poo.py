def validar_senha(senha):
    return len(senha) >= 8

print(validar_senha("12345678"))
print(validar_senha("abc123"))
