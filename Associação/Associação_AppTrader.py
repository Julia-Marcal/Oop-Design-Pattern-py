from typing import Type

class AppTrader:
    def __init__(self, name_account: str):
        self.__name_account = name_account
        self.__nome_crypto = None

    @property
    def name_account(self):
        return self.__name_account

    @property
    def nome_crypto(self):
        return self.__nome_crypto
        #use property because it's private 

    @nome_crypto.setter
    def nome_crypto(self, n_cont):
        self.__nome_crypto = n_cont    


    def buy(self):
        print(f"Selling {self.__nome_crypto}")

    def sell(self):
        print(f"Buying {self.__nome_crypto}")


class Account:
    def __init__(self, name: Type[AppTrader]) -> None:
        self.name = name

    def conta_comprar(self, trader: Type[AppTrader]):
        trader.buy()

    def conta_vender(self, trader: Type[AppTrader]):
        trader.sell()

class Crypto:
    #def __init__(self, name_m):
        #self.__name_m = name_m
    
    #@property
    #def name_m(self):
        #return self.__name_m

    def add_crypto(self):
        print(f'Adding...')


app_blockchain = AppTrader('Geovana_hck')
shiba_inu = Crypto()
app_blockchain.nome_crypto(shiba_inu)