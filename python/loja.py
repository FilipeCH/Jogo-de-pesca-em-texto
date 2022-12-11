# =============================================linhas============================================= #

def linha():
    print("="*32)

# =============================================loja============================================= #

class Loja:
    def __init__(self, personagem, conta_do_banco):
        
        self._nome_da_loja = "loja de vara"
        self._preco_da_vara, self._codigo_de_compra = self.varas()
        self._escolha = self.escolha()
        self._nome, self._genero, self._idade = personagem
        self._banco = conta_do_banco
        
        if (self._escolha == 1):
            self.ver_estoque()
        elif (self._escolha == 2):
            self.comprar_vara()
    
# =============================================escolher_se_vai_comprar_ou_olhara============================================= #

    def escolha(self):
        escolha = 0
        while (escolha != 1) or (escolha != 2):
            print("[1] ver o estoque | [2] comprar uma vara nova")
            escolha = int(input("faça sua escolha: "))
            if (escolha == 1) or (escolha == 2):
                return escolha        
# =============================================ver_estoque============================================= #
    
    def ver_estoque(self):
        linha()
        print(self._preco_da_vara)
        linha()

# =============================================comprar_varas============================================= #
    
    def comprar_vara(self):
        linha()
        print(self._preco_da_vara)
        linha()
        print("o que deseja compra")
        print(f"{self._codigo_de_compra}")
        o_que_compra = int(input("o que deseja comprar: "))
        
        if (o_que_compra == 1):
            self._banco.pagar(10)
        elif (o_que_compra == 2):
            self._banco.pagar(20)
        elif (o_que_compra == 3):
            self._banco.pagar(30)
        elif (o_que_compra == 4):
            self._banco.pagar(40)
        elif (o_que_compra == 5):
            self._banco.pagar(0)

# =============================================varas============================================= #
    
    def varas(self):
        
        varas_preco = {
            "Vara de iniciante": 10,
            "vara de bambu": 20,
            "vara de fibra de vidro": 30,
            "vara de fibra de carbono": 40,
            "vara de adm": 0
            }
        varas_codigo_de_compra = {
            1:"Vara de iniciante",
            2:"vara de bambu",
            3:"vara de fibra de vidro",
            4:"vara de fibra de carbono",
            5:"vara de adm"
        }
        return varas_preco, varas_codigo_de_compra

