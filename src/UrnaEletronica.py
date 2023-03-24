class UrnaEletronica:
    def __init__(self):
        self.candidatos = [{"nome_candidato": "Julio", "partido": "A"}]
    
    def exibe_candidatos(self):
        posicao = 1
        for candidato in self.candidatos:
            #nome do candidato
            print(str(posicao)+"º candidato: "+candidato.get("nome_candidato"),end=" ")
            #partido do candidato
            print("| Partido: "+candidato.get("partido"),end="\n\n")
            posicao += 1
            
    
    def adiciona_candidatos(self, candidato_novo, partido_novo):
        self.candidatos.append({"nome_candidato": candidato_novo, "partido": partido_novo})
    
    def remover_ultimo_candidato(self):
        self.candidatos.pop()

    def atualizar_candidato(self,indice_candidato, chave, valor):
        self.candidatos[indice_candidato] = ({"nome_candidato":chave, "partido":valor})

urna = UrnaEletronica()

def adicionar_candidatos_na_urna():
    numero_de_candidatos = int(input("Quantos candidatos deseja adicionar?: "))
    if numero_de_candidatos != 0:
        for i in range(numero_de_candidatos):
            nome_do_candidato = input("Digite o nome do "+str(i+1)+"º candidato:")
            nome_do_partido = input("Digite o nome do partido do candidato "+nome_do_candidato+":")
            urna.adiciona_candidatos(nome_do_candidato,nome_do_partido)

def atualizar_candidatos_na_urna():
    urna.exibe_candidatos()
    posicao_da_lista =int(input("da lista acima, escolha a posição que deseja atualizar as informações do candidato: "))
    novo_candidato = input("Digite o nome atualizado para o candidato:")
    novo_partido = input("digite o nome atualizado para o partido:")
    urna.atualizar_candidato(posicao_da_lista-1,novo_candidato,novo_partido)

def exibir_menu_da_urna():
    print("------MENU------")
    print("1 - Exibir candidatos")
    print("2 - Adicionar candidatos")
    print("3 - Atualizar candidato existente")
    print("4 - remover ultimo candidato adicionado")
    selecao_do_menu = int(input("Digite a opção do menu acima para realizar a ação descrita:"))

    while not(selecao_do_menu == 1 or selecao_do_menu == 2 or selecao_do_menu == 3 or selecao_do_menu == 4):
        selecao_do_menu = int(input("Por favor, digite um valor condizente com as opções do menu: "))

    if selecao_do_menu == 1:
        urna.exibe_candidatos()

    if selecao_do_menu == 2:
        adicionar_candidatos_na_urna()

    if selecao_do_menu == 3:
        atualizar_candidatos_na_urna()

    if selecao_do_menu == 4:
        urna.remover_ultimo_candidato()



print("Bem vindo a simulação de uma Urna Eletrônica")

exibir_menu_da_urna()

while True:
    confirmar_repeticao = input("deseja realizar outra operação na urna? [S/N]:")
    while confirmar_repeticao != 'S' and confirmar_repeticao != 'N':
        confirmar_repeticao = input("Por favor, digite um valor condizente com as opções do menu: ")
    if confirmar_repeticao == 'S':
        exibir_menu_da_urna()
    elif confirmar_repeticao == 'N':
        print("Obrigado por Utilizar a urna eletrônica !")
        break
print("****************************************************************")
#EMBAIXO SE ENCONTRA O CODIGO ESCRITO NA AULA

#urna.adiciona_candidatos("Hernesto","Honesto")
#adicionar_candidatos_na_urna()


#urna.remover_ultimo_candidato()

#urna.atualizar_candidato(0, "Jaime", "valor")
#atualizar_candidatos_na_urna()