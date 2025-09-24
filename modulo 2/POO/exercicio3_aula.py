class FormaGeometrica:
    def __init__(self,cor):
        self.cor = cor


    def calcular_area(self):
        pass



class Retangulo(FormaGeometrica):
    def __init__(self, cor,largura,altura):
        super().__init__(cor)
        self.__largura = largura
        self.__altura = altura



    def calcular_area(self):
        return self.__largura * self.__altura
    


class Quadrado(Retangulo):
    def __init__(self, cor,lado):
        super().__init__(cor,lado, lado)
        

def calcular_soma_areas(formas):
    soma = 0
    for forma in formas:
        area = forma.calcular_area()  
        print(f"Área da {forma.__class__.__name__}: {area}")
        soma += area
    print(f"Soma total das áreas: {soma}")


if __name__ == "__main__":
    ret = Retangulo("azul", 4, 5)
    quad = Quadrado("vermelho", 3)

    formas = (ret, quad)

    calcular_soma_areas(formas)