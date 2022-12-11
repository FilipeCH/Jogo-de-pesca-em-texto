# =============================================import============================================= #

from random import randrange

# =============================================class============================================= #

class Personagem:
    def __init__(self):
        self._nome, self._genero, self._idade = self.cria_personagem()
        self._abilidades = self.define_abilidades()
        self._vara_de_persca = None

# =============================================metodo_str============================================= #

    def __str__(self):
        return f"Nome: {self._nome} | Genero: {self._genero} | Idade: {self._idade} | abilidades: {self._abilidades} | vara atual: {self._vara_de_persca}"

# =============================================retorna_o_nome_do_personagem============================================= #

    def dados_do_personagem(self):
        return self._nome, self._genero, self._idade

# =============================================cria_o_personagem============================================= #

    def cria_personagem(self):
        nome = str(input("Qual e o seu nome: ")).capitalize()
        genero = str(input("Qual e o seu genero [F/M]: ")).upper()
        idade = int(input("Qual sua idade: "))
        return nome, genero, idade

# =============================================abilidades============================================= #

    def define_abilidades(self):
        abilidades = dict()

        # define as abilidade
        abilida_de_pesca = randrange(1, 5)
        persoazao = randrange(1, 5)

        abilidades["abilidade de pesca"] = abilida_de_pesca
        abilidades["persoazão"] = persoazao

        return abilidades

