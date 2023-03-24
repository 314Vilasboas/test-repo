from monstro import Monstro


class Goblin(Monstro):
    def __init__(self, inteligencia_do_goblin,pontos_de_ataque,pontos_de_vida,tamanho_do_goblin):
        super().__init__(tipo_do_monstro="Goblin",pontos_de_ataque=pontos_de_ataque,pontos_de_vida=pontos_de_vida)
        self.inteligencia = inteligencia_do_goblin
        self.tamanho = tamanho_do_goblin