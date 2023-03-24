from monstro import Monstro


class Lobo(Monstro):
    def __init__(self, forca_do_lobo,pontos_de_ataque,pontos_de_vida,tamanho_do_lobo):
        super().__init__(tipo_do_monstro="Lobo",pontos_de_ataque=pontos_de_ataque,pontos_de_vida=pontos_de_vida)
        self.forca = forca_do_lobo
        self.tamanho = tamanho_do_lobo

    def receber_dano(self, dano):
        super().receber_dano(dano - self.forca)