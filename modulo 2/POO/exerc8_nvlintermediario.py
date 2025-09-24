class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.nivel_combustivel = 0

    def abastecer(self, litros):
        if litros > 0:
            self.nivel_combustivel += litros
            print(
                f"Abastecido com {litros} litros.",
                "Nível atual: {self.nivel_combustivel:.2f} litros.",
            )
        else:
            print("Quantidade de litros inválida.")

    def dirigir(self, distancia):
        consumo_por_km = 1 / 10
        combustivel_necessario = distancia * consumo_por_km

        if combustivel_necessario <= self.nivel_combustivel:
            self.nivel_combustivel -= combustivel_necessario
            print(
                f"O carro {self.modelo} andou {distancia} km. Combustível restante: {self.nivel_combustivel:.2f} litros."
            )
        else:
            print(
                f"Combustível insuficiente para andar {distancia} km. Nível atual: {self.nivel_combustivel:.2f} litros."
            )


if __name__ == "__main__":
    carro1 = Carro("Fusca")

    carro1.abastecer(5)
    carro1.dirigir(30)
    carro1.dirigir(30)
