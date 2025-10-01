from estudante import Estudante
from escola import Escola



escola = Escola('HMS')
estudante1 = Estudante('Matheus',21,100123)
estudante2 = Estudante('Anderson',35,402439)

estudante1.adicionar_nota('Matematica',8)
estudante1.adicionar_nota('Quimica',8)
estudante1.adicionar_nota('Fisica',10)

estudante2.adicionar_nota('Portugues',4)
estudante2.adicionar_nota('Ingles',10)
estudante2.adicionar_nota('Geografia',3)


escola.adicionar_estudante(estudante1)
escola.adicionar_estudante(estudante2)

escola.mostrar_relatorio()