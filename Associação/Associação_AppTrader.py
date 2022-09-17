from typing import Type

class AppTrader:
    def __init__(self, name_account: str):
        self.__name_account = name_account
        self.__nome_crypto = None

    @property
    def name_account(self):
        return self.__name_account
        #use property(getter) because it's private 
        #the value can't be accessed out of the scope of the class

    @property
    def nome_crypto(self):
        return self.__nome_crypto 

    @nome_crypto.setter
    def nome_crypto(self, nome_crypto):
        self.__nome_crypto = nome_crypto


    def sell(self):
        if self.nome_crypto == None:
            print('Error')
        else:
            print(f"Selling")

    def buy(self):
        if self.nome_crypto == None:
            print('Error')
        else:
            print(f"Buying")


class Account:
    def account_buy(trader: Type[AppTrader]):
        trader.buy()

    def account_sell(trader: Type[AppTrader]):
        trader.sell()

class Crypto:
    def __init__(self, name_of_crypto: str):
        self.name_of_crypto = name_of_crypto

    def add_crypto(self):
        print(f'Adding {self.name_of_crypto} coin on the database of AppTrader...')


cc = AppTrader('Hacker01')
#name of account of app

acc_action = Account
#creating account that could be used at the future

coin = Crypto('Shiba')
#giving a name to crypto on Crypto() and on the setter of AppTrader

cc.nome_crypto = coin
cc.nome_crypto.add_crypto()
acc_action.account_buy(cc)
