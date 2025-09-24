class Cachorro:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def latir(self,fala:str) -> None:
        print(f'{self.nome} diz:{fala}')


meu_cachorro = Cachorro('Rex','preto')

print(meu_cachorro.nome)
print(meu_cachorro.cor)

meu_cachorro.latir("Au Au")
