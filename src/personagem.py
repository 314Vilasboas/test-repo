
from servivo import SerVivo


class Personagem(SerVivo):
    def __init__(self, nome_do_personagem,pontos_de_vida,pontos_de_ataque):
        super().__init__(pontos_de_vida,pontos_de_ataque)
        self.nome = nome_do_personagem
 