import abc
from abc import ABC, abstractmethod

class Veiculo(ABC):
    __slots__ = ['_placa', '_ano']

    def __init__(self, placa='', ano=0):
        self.placa = placa
        self.ano = ano

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @abstractmethod
    def exibirDados(self):
        pass

    @abstractmethod
    def teste(self):
        pass

"""
    def exibeDados(self):
        return f'Placa: {self._placa}, Ano: {self._ano}'
"""

class Onibus(Veiculo):
    __slots__ = ['_assentos']

    def __init__(self, placa, ano, assentos):
        super().__init__(placa, ano)
        self.assentos = assentos

    @property
    def assentos(self):
        return self._assentos

    @assentos.setter
    def assentos(self, assentos):
        self._assentos = assentos

    def exibirDados(self):
        return f'Placa: {self._placa}, Ano: {self._ano}, Assentos: {self._assentos}'


class Caminhao(Veiculo):
    __slots__ = ['_eixos']

    def __init__(self, placa, ano, eixos):
        super().__init__(placa, ano)
        self.eixos = eixos

    @property
    def eixos(self):
        return self._eixos

    @eixos.setter
    def eixos(self, eixos):
        self._eixos = eixos


    def exibirDados(self):
        return f'Placa: {self._placa}, Ano: {self._ano}, Assentos: {self._assentos}'