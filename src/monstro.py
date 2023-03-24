from servivo import SerVivo


class Monstro(SerVivo):
    def __init__(self, tipo_do_monstro,pontos_de_vida,pontos_de_ataque):
        super().__init__(pontos_de_vida,pontos_de_ataque)
        self.tipo = tipo_do_monstro