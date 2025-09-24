from exerc5_nvlbasico import ContaBancaria


class ContaBancariaComSaque(ContaBancaria):
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")


if __name__ == "__main__":
    conta1 = ContaBancariaComSaque("Matheus", 1000)

    print("Saldo inicial:")
    conta1.exibir_saldo()

    print("\nDepósito de 500:")
    conta1.depositar(500)
    conta1.exibir_saldo()

    print("\nSaque de 800 (bem-sucedido):")
    conta1.sacar(800)
    conta1.exibir_saldo()

    print("\nSaque de 1000 (saldo insuficiente):")
    conta1.sacar(1000)
    conta1.exibir_saldo()
