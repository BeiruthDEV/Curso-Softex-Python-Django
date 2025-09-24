class Funcionario:
    percentual_bonus = 1.10

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aplicar_bonus(self):
        self.salario *= Funcionario.percentual_bonus
        print(f"{self.nome} recebeu bônus! Novo salário: R${self.salario:.2f}")


if __name__ == "__main__":
    func1 = Funcionario("Ana", 2000)
    func2 = Funcionario("Bruno", 3000)

    print("Salários antes do bônus:")
    print(f"{func1.nome}: R${func1.salario:.2f}")
    print(f"{func2.nome}: R${func2.salario:.2f}")

    print("\nAplicando bônus...")
    func1.aplicar_bonus()
    func2.aplicar_bonus()
