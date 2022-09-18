from os import system

class Computer:
    def __init__(self) -> None:
        self.bd_list = []


    def insert_on_bd(self, system, year):
        self.bd_list.append(Info_computer(system, year))
        for i in self.bd_list:
            print(i.system, i.year)
    


class Info_computer:
    def __init__(self, system:str , year: int) -> None:
        self.system = system
        self.year = year


c1 = Computer()
c1.insert_on_bd('apple', 2008)