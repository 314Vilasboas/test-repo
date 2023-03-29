from conta import conta

class contaPoupanca(conta):
    def __init__(self, titular, saldo) -> None:
        super().__init__(titular, saldo)

        #essas 3 taxas de rendimento abaixo foram pegas na internet sobre o rendimento anual, mensal e diário de uma conta
        #poupança no Brasil no dia 28 de março de 2023.

        self.taxa_rendimento_anual = 6.17/100           
        self.taxa_rendimento_mensal = 0.5/100           
        self.taxa_rendimento_diaria = 0.022/100         
        
        #Como não encontrei valores oficiais para as taxas de rendimento abaixo, tomei a liberdade de usar a taxa diária oficial
        #como base para formulas de criação para essas novas taxas.
        
        self.taxa_rendimento_hora = self.taxa_rendimento_diaria/24
        self.taxa_rendimento_minuto = self.taxa_rendimento_hora/60
        self.taxa_rendimento_segundo = self.taxa_rendimento_minuto/60

    def depositar(self, deposito):
        if deposito <= 0:
            raise ValueError("Valor do depósito invalido!")
        else:
            self.saldo_da_conta += deposito
    
    def sacar(self, saque):
        if (self.saldo_da_conta - saque) < 0:
            raise ValueError("Valor do saque superior ao valor do saldo")
        else:
            self._atualizar_saldo(saque)

    def _atualizar_saldo(self, saque):
        self.saldo_da_conta = self.saldo_da_conta - saque
        print(f"Sr(a) {self.titular_da_conta}, seu novo saldo é: {self.saldo_da_conta:.2f}")

    def consultar_poupanca(self):

        print(f"Senhor(a) {self.titular_da_conta}, deseja visualizar o rendimento em qual período de tempo?")
        print("1 - Anos")
        print("2 - Meses")
        print("3 - Dias")
        print("4 - Horas")
        print("5 - Minutos")
        print("6 - Segundos")
        menu_rendimento = int(input("Digite o numero correspondente a opção desejada:"))

        if menu_rendimento == 1:
            quantidade_anos = int(input("por quantos anos deseja testar o rendimento?: "))
            valor_poupanca = self.saldo_da_conta
            
            for _ in range(quantidade_anos):
                valor_poupanca = valor_poupanca + (valor_poupanca*self.taxa_rendimento_anual)
            
            print(f"{valor_poupanca:.2f}")   

        if menu_rendimento == 2:
            quantidade_meses = int(input("por quantos meses deseja testar o rendimento?: "))
            valor_poupanca = self.saldo_da_conta

            for _ in range(quantidade_meses):
                valor_poupanca = valor_poupanca + (valor_poupanca*self.taxa_rendimento_mensal)
        
            print(f"{valor_poupanca:.2f}")
        
        if menu_rendimento == 3:
            
            quantidade_dias = int(input("por quantos dias deseja testar o rendimento?: "))
            valor_poupanca = self.saldo_da_conta

            for _ in range(quantidade_dias):
                valor_poupanca = valor_poupanca + (valor_poupanca*self.taxa_rendimento_diaria)
        
            print(f"{valor_poupanca:.2f}")  

        if menu_rendimento == 4:
            quantidade_horas = int(input("por quantas horas deseja testar o rendimento?: "))
            valor_poupanca = self.saldo_da_conta

            for _ in range(quantidade_horas):
                valor_poupanca = valor_poupanca + (valor_poupanca*self.taxa_rendimento_hora)
        
            print(f"{valor_poupanca:.4f}")  

        if menu_rendimento == 5:
            quantidade_minutos = int(input("por quantos minutos deseja testar o rendimento?: "))
            valor_poupanca = self.saldo_da_conta

            for _ in range(quantidade_minutos):
                valor_poupanca = valor_poupanca + (valor_poupanca*self.taxa_rendimento_minuto)
        
            print(f"{valor_poupanca:.5f}")

        if menu_rendimento == 6:
            quantidade_segundos = int(input("por quantos segundos deseja testar o rendimento?: "))
            valor_poupanca = self.saldo_da_conta

            for _ in range(quantidade_segundos):
                valor_poupanca = valor_poupanca + (valor_poupanca*self.taxa_rendimento_segundo)
            
            print(f"{valor_poupanca:.7f}")  
             