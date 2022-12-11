# =============================================import============================================= #

from random import randrange

# =============================================class============================================= #

class Personagem:
    def __init__(self):
        self._nome, self._genero, self._idade = self.cria_personagem()
        self._abilidades = self.define_abilidades()
        self._vara_de_persca = None
        self._invetario_de_peixe = dict()

# =============================================metodo_str============================================= #

    def __str__(self):
        return f"Nome: {self._nome} | Genero: {self._genero} | Idade: {self._idade} | abilidades: {self._abilidades} | vara atual: {self._vara_de_persca}"

# =============================================cria_o_personagem============================================= #

    def cria_personagem(self):
        nome = str(input("Qual e o seu nome: ")).capitalize()
        genero = str(input("Qual e o seu genero [F/M]: ")).upper()
        idade = int(input("Qual sua idade: "))
        return nome, genero, idade

    def define_abilidades(self):
        abilidades = dict()

        # define as abilidade
        abilida_de_pesca = randrange(1, 5)
        persoazao = randrange(1, 5)

        abilidades["abilidade de pesca"] = abilida_de_pesca
        abilidades["persoazão"] = persoazao

        return abilidades

# =============================================retorna_dados_do_personagem============================================= #

    def dados_do_personagem(self):
        return self._nome, self._genero, self._idade

    def abilidade_e_vara(self):
        return self._abilidades, self._vara_de_persca

# =============================================adiciona_peixe============================================= #

    def adiciona_peixe(self, peixe, valor):
        self._invetario_de_peixe[peixe] = valor