from conta import conta 

class contaCorrente(conta):
    def __init__(self, titular, saldo, limite) -> None:
        super().__init__(titular, saldo)

        self.limite_da_conta = limite
    
    def depositar(self, deposito):
        if deposito <= 0:
            raise ValueError("Valor do depósito invalido!")
        else:
            self.saldo_da_conta += deposito

    def sacar(self, saque):
        valor_total_para_saque = self.saldo_da_conta + self.limite_da_conta
        
        if (valor_total_para_saque - saque) < 0:
            raise ValueError("Valor do saque superior ao saldo + limite")
        else:
            self._atualizar_saldo(saque)
  
    def _atualizar_saldo(self, saque):
        if self.saldo_da_conta > 0 and self.limite_da_conta > 0:
            if ((self.saldo_da_conta - saque) >= 0):    
                self.saldo_da_conta = self.saldo_da_conta - saque
                print(f"Saque realizado Sr(a). {self.titular_da_conta}! seu novo saldo é: {self.saldo_da_conta:.2f}")
            else:
                print(self.saldo_da_conta - saque)
                self.limite_da_conta -= abs(self.saldo_da_conta - saque)
                print(self.limite_da_conta)
                self.saldo_da_conta = 0
                print(f"Saque realizado Sr(a). {self.titular_da_conta}! seu novo saldo é: {self.saldo_da_conta:.2f}")
                print(f"Sr(a). {self.titular_da_conta}, AVISO! seu saldo zerou e foi utilizado o Limite!\nSeu novo Limite é:{self.limite_da_conta:.2f}")
        
        elif self.saldo_da_conta == 0 and self.limite_da_conta > 0:
            self.limite_da_conta -= saque
            print(f"Sr(a). {self.titular_da_conta}, AVISO! seu saldo está vazio e foi utilizado o Limite!\nSeu novo Limite é:{self.limite_da_conta:.2f}")

        elif self.saldo_da_conta > 0 and self.limite_da_conta == 0:
            self.saldo_da_conta -= saque
            print(f"Saque realizado Sr(a). {self.titular_da_conta}! seu novo saldo é: {self.saldo_da_conta:.2f}")