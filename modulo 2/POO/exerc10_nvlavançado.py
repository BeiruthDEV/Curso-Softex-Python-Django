class Motor:
    def __init__(self, potencia):
        self.potencia = potencia


class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo

        self.motor = Motor(potencia_motor)

    def exibir_potencia(self):
        print(f"O carro {self.modelo} tem {self.motor.potencia} cavalos de potência.")


if __name__ == "__main__":
    carro1 = Carro("Fusca", 50)
    carro2 = Carro("Mustang", 450)

    carro1.exibir_potencia()
    carro2.exibir_potencia()
