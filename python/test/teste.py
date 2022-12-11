from random import randrange


def define_abilidades():
    abilidades = dict()

    # define as abilidade
    abilida_de_pesca = randrange(1, 5)
    persoazao = randrange(1, 5)

    abilidades["abilidade de pesca"] = abilida_de_pesca
    abilidades["persoazão"] = persoazao

    print(abilidades["abilidade de pesca"])

define_abilidades()