# =============================================are_de_import============================================= #

# =============================================class============================================= #
def linha():
    print("="*32)

class Banco:
    def __init__(self, dados_do_personagem):
        self._nome, self._idade, self._genero = dados_do_personagem
        self._saldo = 1000
    
# =============================================mostra_os_dados============================================= #

    def __str__(self):
         return f"Nome: {self._nome} | Idade: {self._idade} | Genero: {self._genero} | saldo: {self._saldo}"

# =============================================depositar_dinheiro============================================= #

    def depositar(self, valor):
        self._saldo += valor
        return self._saldo

# =============================================pagar_algo============================================= #

    def pagar(self, valor):
        self._saldo -= valor
        return self._saldo