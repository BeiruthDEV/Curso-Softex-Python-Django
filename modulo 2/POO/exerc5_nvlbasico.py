class ContaBancaria:
    def __init__(self,titular,saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial



    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f'Deposito de R${valor:.2f} realizado com sucesso')

        else:
            print("Valor de depósito inválido")
        