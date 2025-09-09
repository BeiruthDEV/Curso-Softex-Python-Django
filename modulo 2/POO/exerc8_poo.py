def verificar_login(usuario: str, senha: str) -> str:
    if usuario == "admin" and senha == "12345":
        return "Acesso concedido"
    else:
        return "Acesso negado"

print(verificar_login("admin", "12345"))  
print(verificar_login("user", "0000"))    
