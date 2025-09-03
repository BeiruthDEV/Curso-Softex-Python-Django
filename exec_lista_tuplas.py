vendas =    [
    ("Teclado", 50,2),
    ("Mouse", 25.50, 4),
    ("Monitor", 300,1),
    ("Fone",45,1),
    ("Webcam", 75.20,2)
]
vendas_filtradas = [v for v in vendas if v[1] * v[2] >=100]
produtos_unicos = {v[0] for v in vendas}
print("\nVendas filtradas com valor maior ou igual a 100:")
print(vendas_filtradas)

print('\nProdutos unicos:')
print(produtos_unicos)