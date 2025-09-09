from exerc11_poo import IMCCalculadora

class IMCClassificador:
    @staticmethod
    def classificar_imc(imc: float) -> str:
        if imc < 18.5:
            return "Abaixo do peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidade"

if __name__ == "__main__":
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em metros: "))
    imc = IMCCalculadora.calcular_imc(peso, altura)
    print("Seu IMC é:", imc)
    print("Classificação:", IMCClassificador.classificar_imc(imc))
