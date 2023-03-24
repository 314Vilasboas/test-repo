
#classe ser vivo, base pro projeto. TODOS os personagens
#serão seres vivos, Atributos de Pontos de vida e pontos de ataque
#classes derivadas do ser vivo, Personagem e monstro.

#personagem atributo adicional nome
#monstro atributo adicional tipo

#mais duas classes derivadas de monstro, Lobo e Goblin
#lobo possui atributo adicional força
#goblin possui atributo adicional inteligencia

#funcao primeiro parametro, dano causado e segundo parametro,
#quem vai receber esse dano


import random

from personagem import Personagem
from goblin import Goblin
from lobo import Lobo

def batalha(pessoa,monstro):
    print("Batalha entre "+pessoa.nome+" e "+monstro.tipo+" irá começar:")
    #decidir quem bate e quem apanha primeiro
    primeiro_agressor = random.randint(0,1)
    if primeiro_agressor == 0:
        #o personagem ataca primeiro
        executar_dano(pessoa,monstro)
        print(pessoa.nome +" deixou o "+ monstro.tipo +" com "+str(monstro.vida) +" pontos de vida")
    if primeiro_agressor == 1:
        #o monstro ataca primeiro
        executar_dano(monstro,pessoa)
        print(monstro.tipo +" deixou o "+ pessoa.nome +" com "+str(pessoa.vida) +" pontos de vida")
    
def executar_dano(agressor,agredido):
    agredido.receber_dano(agressor.inflingir_dano())  


def gerar_personagem():
    vida_personagem = int(input("digite a vida do personagem: "))
    ataque_personagem = int(input("digite o ataque do personagem: "))
    nome_personagem = input("digite o nome do personagem: ")

    personagem = Personagem(nome_personagem,vida_personagem,ataque_personagem)
    return personagem

def gerar_monstro():
    vida_monstro = int(input("digite a vida do monstro: "))
    ataque_monstro = int(input("digite o ataque do monstro: "))
    indice_tamanho = random.randint(1,3)
   
    if indice_tamanho == 1:
        tamanho_monstro = "pequeno"
    if indice_tamanho == 2:
        tamanho_monstro = "médio"
    if indice_tamanho == 3:
        tamanho_monstro = "Grande"

    print("selecione o tipo:")
    print("1 - Lobo")
    print("2 - goblin")
    selecao_do_tipo = int(input("selecione: "))

    if selecao_do_tipo == 1:
        forca = int(input("digite a força do Lobo: "))
        monstro = Lobo(forca,ataque_monstro,vida_monstro,tamanho_monstro)
    if selecao_do_tipo == 2:
        inteligencia = int(input("digite a inteligencia do Goblin: "))
        monstro = Goblin(inteligencia,ataque_monstro,vida_monstro,tamanho_monstro)

    return monstro

print("Bem vindo a simulação de uma batalha de RPG básica!")

print("Primeiro, crie o personagem")

ser_vivo_personagem = gerar_personagem()

print("Agora, crie um monstro")

ser_vivo_monstro = gerar_monstro()

print("agora um embate ocorrerá")

batalha(ser_vivo_personagem,ser_vivo_monstro)