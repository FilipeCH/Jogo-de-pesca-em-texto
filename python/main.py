# Jogo de pesca

# =============================================import============================================= #

from personagem import Personagem
from banco import Banco
from loja import Loja

# =============================================Personagem============================================= #

personagem1 = Personagem()
dados_do_personagem = personagem1.dados_do_personagem()
personagem1_banco = Banco(dados_do_personagem)
print(personagem1_banco)

personagem1_loja = Loja(dados_do_personagem, personagem1_banco)
print(personagem1_banco)