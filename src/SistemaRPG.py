

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




from personagem import Personagem
from goblin import Goblin
from lobo import Lobo


bruxo = Personagem("Geraldo",1000,100)

wolfgang = Lobo(80,40,420,"Grande")

gilderlang = Goblin(70,20,210,"Pequeno")

def batalha(pessoa,monstro):
    print("Batalha entre "+pessoa.nome+" e "+monstro.tipo+" irá começar:")
    dar_dano(pessoa,monstro)
    
def dar_dano(agressor,agredido):
    agredido.vida = agredido.vida - agressor.ataque
    print("a vida ficou: "+str(agredido.vida))

def receber_dano():
    pass
batalha(bruxo,wolfgang)



