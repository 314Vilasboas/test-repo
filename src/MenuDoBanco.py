from contabancaria import ContaDoBanco

class usuario (ContaDoBanco):
    def boas_vindas_cliente(self):
        print("Olá "+self.titular+"! Bem-vindo a sua conta bancária.")
        iniciar_menu()

def iniciar_menu():
    print("qual função que deseja realizar: ")
    print("1 - Depositar valor")
    print("2 - Sacar um valor")
    print("3 - consultar seu saldo")

    selecao_do_menu = int(input("Digite o número correspondente com a função: "))
    while not(selecao_do_menu == 1 or selecao_do_menu == 2 or selecao_do_menu == 3):
        selecao_do_menu = int(input("Por favor, digite um valor condizente com as opções do menu: "))

    if selecao_do_menu == 1:
        valor_do_deposito = float(input("digite o valor a ser depositado:"))
        while valor_do_deposito <= 0:
            valor_do_deposito = float(input("Por favor, digite um valor maior que Zero para depositar: "))
        titular_da_conta.depositar(valor_do_deposito)
        titular_da_conta.consultar_saldo()

    if selecao_do_menu == 2:
        valor_do_saque = float(input("Digite o valor a ser sacado:"))
        while valor_do_saque > titular_da_conta.saldo:
            valor_do_saque = float(input("Por favor, digite um valor menor ou igual ao saldo para sacar: "))
        titular_da_conta.sacar(valor_do_saque)
        titular_da_conta.consultar_saldo()

    if selecao_do_menu == 3:
        titular_da_conta.consultar_saldo()

nome_do_titular = input("Para começar essa simulação digite um nome para o titular da conta:")
saldo_do_titular = float(input("Agora, digite um valor inicial para o saldo do titular: "))

titular_da_conta = usuario(nome_do_titular,saldo_do_titular)
titular_da_conta.boas_vindas_cliente()

while True:
    confirmar_repeticao = input("deseja realizar outra operação bancária? [S/N]:")
    while confirmar_repeticao != 'S' and confirmar_repeticao != 'N':
        confirmar_repeticao = input("Por favor, digite um valor condizente com as opções do menu: ")
    if confirmar_repeticao == 'S':
        iniciar_menu()
    elif confirmar_repeticao == 'N':
        print("Obrigado por Utilizar os Serviços do banco!")
        break
