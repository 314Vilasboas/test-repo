from contaCorrente import contaCorrente
from contaPoupanca import contaPoupanca

conta = None

def realizar_deposito(conta_do_titular):
    while True:
        deposito = float(input("Digite o valor que deseja depositar: "))
        try:
            while type(deposito) != float:
                deposito = float(input("Digite um valor numérico: "))
            conta_do_titular.depositar(deposito)
        except ValueError as ve:
            print(ve)
        
        confirma_repeticao = input("Você deseja fazer mais um depósito?[S/N]:")
        while confirma_repeticao != 'S' and confirma_repeticao != 'N':
            confirma_repeticao = input("Por favor, digite um valor condizente com as opções do menu: ")
        
        if confirma_repeticao == 'N':
            break

def realizar_saque(conta_do_titular):
    while True:
        saque = float(input("Digite o valor que deseja sacar: "))
        try:
            while type(saque) != float:
                saque = float(input("Digite um valor numérico: "))
            conta_do_titular.sacar(saque)  
        except ValueError as ve:
            print(ve)
          
        confirma_repeticao = input("Você deseja fazer mais um saque?[S/N]:")
        while confirma_repeticao != 'S' and confirma_repeticao != 'N':
            confirma_repeticao = input("Por favor, digite um valor condizente com as opções do menu: ")
        
        if confirma_repeticao == 'N':
            break

def checar_poupanca(conta_do_titular):
    while True:
        conta_do_titular.consultar_poupanca()
        confirma_repeticao = input("Você deseja fazer mais uma consulta?[S/N]:")
        while confirma_repeticao != 'S' and confirma_repeticao != 'N':
            confirma_repeticao = input("Por favor, digite um valor condizente com as opções do menu: ")
        
        if confirma_repeticao == 'N':
            break

def criar_menu_conta_poupanca():
    while True:
        print(f"SALDO:{conta.saldo_da_conta:.2f}")
        print("1 - saque")
        print("2 - depósito")
        print("3 - consultar rendimento da poupança")
        print("4 - Finalizar")
        opcao = int(input("opção: "))
        while opcao !=1 and opcao !=2 and opcao !=3 and opcao !=4:
            opcao = int(input("Por favor, digite um valor condizente com as opções do menu: "))

        if opcao == 1:
            realizar_saque(conta)
        if opcao == 2:
            realizar_deposito(conta)
        if opcao == 3:
            checar_poupanca(conta)
        if opcao == 4:
            print(f"Senhor(a) {conta.titular_da_conta}, Obrigado(a) por utilizar nossos serviços!")
            break

def criar_menu_conta_corrente():
    while True:
        print(f"SALDO:{conta.saldo_da_conta:.2f}")
        print("1 - saque")
        print("2 - depósito")
        print("3 - consultar Limite")
        print("4 - Finalizar")
        opcao = int(input("opção: "))
        while opcao !=1 and opcao !=2 and opcao !=3 and opcao !=4:
            opcao = int(input("Por favor, digite um valor condizente com as opções do menu: "))

        if opcao == 1:
            realizar_saque(conta)
        if opcao == 2:
            realizar_deposito(conta)
        if opcao == 3:
            print(f"Senhor(a) {conta.titular_da_conta}, seu limite é:{conta.limite_da_conta}")
        if opcao == 4:
            print(f"Senhor(a) {conta.titular_da_conta}, Obrigado(a) por utilizar nossos serviços!")
            break

print("Bem vindo a simulação de uma conta bancária")
nome_do_titular = input("Para começar digite o nome do Titular: ")
saldo_inicial = float(input("Agora digite o saldo inicial: "))
Limite_do_titular = float(input("Por fim, digite o limite da conta: "))

menu_criacao_de_conta = int(input("Digite 1 para conta poupança e 2 para conta corrente: "))

if menu_criacao_de_conta == 1:
    conta = contaPoupanca(nome_do_titular,saldo_inicial)
    criar_menu_conta_poupanca()
if menu_criacao_de_conta == 2:
    conta = contaCorrente(nome_do_titular,saldo_inicial,Limite_do_titular)
    criar_menu_conta_corrente()

