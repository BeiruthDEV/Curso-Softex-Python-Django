import math

def circulo(raio):
    area = math.pi * raio ** 2
    circunferencia = 2 * math.pi * raio
    return area, circunferencia

a, c = circulo(5)
print("Área:", a)
print("Circunferência:", c)
