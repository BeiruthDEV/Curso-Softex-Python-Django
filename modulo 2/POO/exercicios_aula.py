class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


    def apresentar(self):
        print(f'Olá, me chamo {self.nome} e tenho {self.idade} anos.')


class Estudante(Pessoa):
    def __init__(self, nome, idade,curso:str):
        super().__init__(nome, idade)
        self.curso = curso


    def apresentar(self):
        print(f'Olá, me chamo {self.nome}, tenho {self.idade} anos e eu curso {self.curso}')



pessoa1 = Pessoa('Matheus',21)
estudante1 = Estudante('Gabriel',25,'Nutrição')


pessoas = [pessoa1,estudante1]


for pessoa in pessoas:
    pessoa.apresentar()
