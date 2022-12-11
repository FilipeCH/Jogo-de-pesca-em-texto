from random import randrange

class pesca:
    def __init__(self, dados_do_personagem):
        self._abilidade, self.vara_atual = dados_do_personagem

    def pescar(self):
        peixe = randrange(0, 7)
        return peixe