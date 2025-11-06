def comprimir_lista(lista_mista):
    lista_numeros = [x for x in lista_mista if isinstance(x, (int, float)) and not isinstance(x, bool)]
    return lista_numeros

dados = [10, "Python", 3.14, True, False, [], 42, "texto"]
resultado = comprimir_lista(dados)
print(f"Lista original: {dados}")
print(f"Lista comprimida (apenas números): {resultado}")