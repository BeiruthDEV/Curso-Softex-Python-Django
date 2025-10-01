class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
        
        
    def get_nome(self):
        return self.nome
    
    
    
pessoa = Pessoa("João",30)

print(pessoa.get_nome())