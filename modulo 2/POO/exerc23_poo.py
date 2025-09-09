usuarios = {
    "admin": "12345",
    "matheus": "senha123"
}

def autenticar(usuario, senha):
    return usuarios.get(usuario) == senha

print(autenticar("admin", "12345"))  # True
print(autenticar("matheus", "errado"))  # False
