class Vehicle:

    def __init__(self, name:str, year:int) ->None:
        self.name = name 
        self.year = year
        self.classname = self.__class__.__name__

    def motor(self) -> None:
        print(f"Vroom vroom I'm a {self.classname}")


class Bicycle(Vehicle):
    def __init__(self, name, year):
        super().__init__(name, year)

    def DocumentationToPay(self):
        print(f'As your vehicle is a {self.classname} you have to pay 1100$ for your documentation')


class Car(Vehicle):
    def __init__(self, name, year):
        super().__init__(name, year)

    def DocumentationToPay(self):
        print(f'As your vehicle is a {self.classname} you have to pay 3000$ for your documentation')


Carro = Car('Mustang', 2010)
Carro.DocumentationToPay()
Carro.motor()
