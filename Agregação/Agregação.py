#one class NEED the other one to work
from itertools import product
from typing import Type


class Product:
    def __init__(self, prod_n: str, prod_val: int) -> None:
        self.__prod_n = prod_n
        self.__prod_val = prod_val

    @property
    def product_value(self):
        return self.__prod_val

    def info_of_product(self):
        print(f'Product: {self.__prod_n} / Value {self.__prod_val} ')


class ShopCart: 
    
    def __init__(self) -> None:
        self.__products_list = []
        self.__value_of_cart = 0

    def add_to_cart(self, produto: Type[Product]):
        self.__products_list.append(produto)
        print('Product added to cart')

    def finalize_purchase(self) -> None:
        print('\nPurchase Finished!')
        x = input('Wanna see the list you bought and how much you have to pay? ')
        x.lower
        if x.startswith('s') or x.startswith('y'):
            print('\n')
            for produto in self.__products_list:
                self.__value_of_cart += produto.product_value
                produto.info_of_product()
            print(f'Total to pay: {self.__value_of_cart}')
        else:
            pass

car = ShopCart()
mon = Product('Monitor', 1000)

car.add_to_cart(mon)
car.finalize_purchase()

