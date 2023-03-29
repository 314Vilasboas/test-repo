class conta:
    def __init__(self, titular, saldo) -> None:
        self.titular_da_conta = titular
        self.saldo_da_conta = saldo
        
    def get_saldo(self):
        return self.saldo_da_conta
    
    def get_titular(self):
        return self.titular_da_conta
    
    def depositar(self, deposito):
        pass

    def sacar(self, saque):
        pass