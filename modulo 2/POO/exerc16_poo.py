def detalhes_produto(nome, **kwargs):
    print(f"Produto: {nome}")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

detalhes_produto("Notebook", preco=3500, marca="Dell", estoque=10)
