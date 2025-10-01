from pessoa import Pessoa
from estudante import Estudante

class Escola:
    def __init__(self,escola):
        self.escola = escola
        self.estudante = []
        
        
    def adicionar_estudante(self,estudante):
        self.estudante.append(estudante)
        
        
        
    def mostrar_relatorio(self):
        print("RELATORIO DE ESTUDANTES")
        print("------------------------")
        for estudante in self.estudante:
            print(f"Nome: {estudante.get_nome()}")
            print(f"Matricula: {estudante.get_matricula()}")
            print("Notas:")
            for materia,notas in estudante.notas.items():
                notas_formatadas = ', '.join(str(nota) for nota in notas)
                print(f' {materia}: {notas_formatadas}')
                
            print('-----------------------')
                
        
        