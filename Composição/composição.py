class Db_computer:
    def __init__(self,system: str, year) -> None:
        self.db_list = []
        self.system = system
        self.year = year

    def insert_on_bd(self):
        self.db_list.append(self.system)
        self.db_list.append(self.year)
        for i in self.db_list:
            print(i)


class Computer:
    def __init__(self, system:str , year: int) -> None:
        self.system_computer = system
        self.year_computer = year
        self.price = None
    
    #getter para mandar as informações para o banco de dados 
    @property
    def return_system(self):
        return self.system_computer
        
    #getter para mandar as informações para o banco de dados 
    @property
    def return_year(self):
        return self.year_computer

    def price_c(self):
        if self.year_computer > 2000 and self.year_computer < 2010:
            self.price = 2000
            print('The price of this pc is: 2000')
        else:
            self.price = 3000
            print('The price of this pc is: 3000')


c1 = Computer('apple', 2008)
c1.price_c()
bd_br = Db_computer(c1.return_system, c1.return_year)
bd_br.insert_on_bd()