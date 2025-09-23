class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco


produto1 = Produto("Caderno",15.50)
produto2 = Produto("Caneta",3.00)

print(f'O primeiro produto é o {produto1.nome} e o preço dele é R${produto1.preco:.2f}')
print(f'O segundo produto é o {produto2.nome} e o preço é R${produto2.preco:.2f}')