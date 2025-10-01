from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = {}
        
    def get_matricula(self):
        return self.matricula
    
    
    def set_matricula(self, matricula):
        self.matricula = matricula
        
    def adicionar_nota(self,materia,nota):
        if materia not in self.notas:
            self.notas[materia] = []  
        self.notas[materia].append(nota)  



estudante = Estudante("Maria", 22, "400293")

estudante.adicionar_nota("Matemática", 9.5)
estudante.adicionar_nota("Matemática", 8.0)


estudante.set_matricula("987654321")


estudante.adicionar_nota("Química", 7.5)



