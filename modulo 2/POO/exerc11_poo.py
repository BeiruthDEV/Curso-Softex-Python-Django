class IMCCalculadora:
    @staticmethod
    def calcular_imc(peso: float, altura: float) -> float:
        return peso / (altura ** 2)

if __name__ == "__main__":
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em metros: "))
    imc = IMCCalculadora.calcular_imc(peso, altura)
    print("Seu IMC é:", imc)
