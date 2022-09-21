#é bom pois não é necessário acoplar codigo nas classes
#só é preciso mudar o factory(staticmethod) que é bem mais simples e facil

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')

class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carrp popular está buscando o cliente...')

class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto está buscando o cliente...')


class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        assert 0, 'Veículo não existe'


if __name__ == "__main__":
    from random import choice
    carros_disponiveis = ['luxo', 'popular', 'moto']

    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()
