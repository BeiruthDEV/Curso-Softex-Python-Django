class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


if __name__ == "__main__":

    ret = Retangulo(5, 3)

    area = ret.calcular_area()
    perimetro = ret.calcular_perimetro()

    print(f"Retângulo de base {ret.base} e altura {ret.altura}:")
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")
