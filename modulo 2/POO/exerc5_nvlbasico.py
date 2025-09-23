class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R${valor:.2f} realizado com sucesso")

        else:
            print("Valor de depósito inválido")

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo atual: R${self.saldo:.2f}")


conta1 = ContaBancaria("Matheus", 1000)

conta1.exibir_saldo()
conta1.depositar(500)
conta1.exibir_saldo()
