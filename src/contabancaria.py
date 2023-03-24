class ContaDoBanco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
    
    def sacar(self, valor):
        if(valor <= self.saldo):
            self.saldo = self.saldo - valor
        else:
            print("saldo é insuficiente!")

    def consultar_saldo(self):
        print(f"saldo atual: R&{self.saldo:.2f}")
