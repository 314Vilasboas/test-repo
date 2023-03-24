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

class SerVivo:
    def __init__(self, pontos_de_vida, pontos_de_ataque):
        self.vida = pontos_de_vida
        self.ataque = pontos_de_ataque
        

class Personagem(SerVivo):
    def __init__(self, nome_do_personagem,pontos_de_vida,pontos_de_ataque):
        super().__init__(pontos_de_vida,pontos_de_ataque)
        self.nome = nome_do_personagem
 

class Monstro(SerVivo):
    def __init__(self, tipo_do_monstro,pontos_de_vida,pontos_de_ataque):
        super().__init__(pontos_de_vida,pontos_de_ataque)
        self.tipo = tipo_do_monstro

class Lobo(Monstro):
    def __init__(self, forca_do_lobo,pontos_de_ataque,pontos_de_vida,tamanho_do_lobo):
        super().__init__(tipo_do_monstro="Lobo",pontos_de_ataque=pontos_de_ataque,pontos_de_vida=pontos_de_vida)
        self.forca = forca_do_lobo
        self.tamanho = tamanho_do_lobo

class Goblin(Monstro):
    def __init__(self, inteligencia_do_goblin,pontos_de_ataque,pontos_de_vida,tamanho_do_goblin):
        super().__init__(tipo_do_monstro="Goblin",pontos_de_ataque=pontos_de_ataque,pontos_de_vida=pontos_de_vida)
        self.inteligencia = inteligencia_do_goblin
        self.tamanho = tamanho_do_goblin

bruxo = Personagem("Geraldo",1000,100)

wolfgang = Lobo(80,40,420,"Grande")

gilderlang = Goblin(70,20,210,"Pequeno")

def batalha(personagem,monstro):
    print("Batalha entre "+personagem.nome+" e "+monstro.tipo+" irá começar:")
    dar_dano(personagem,monstro)
    
def dar_dano(agressor,agredido):
    agredido.vida = agredido.vida - agressor.ataque
    print("a vida ficou: "+str(agredido.vida))

def receber_dano():
    pass
batalha(bruxo,wolfgang)



