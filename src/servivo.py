class SerVivo:
    def __init__(self, pontos_de_vida, pontos_de_ataque):
        self.vida = pontos_de_vida
        self.ataque = pontos_de_ataque

    def inflingir_dano(self):
        return self.ataque

    def receber_dano(self,dano):
        self.vida = self.vida - dano

