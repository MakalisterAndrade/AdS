from abc import ABC, abstractmethod
import math

class Calcs(ABC):

    @abstractmethod
    def calcPerim(self):
        pass

    @abstractmethod
    def calcArea(self):
        pass


class Quadrilatero(Calcs):
    __slots__=['_lado1', '_lado2', '_lado3', '_lado4']

    def __init__(self, lado1, lado2, lado3, lado4):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado4 = lado4

#       super(FormasG, self).__init__()


    @property
    def lado1(self):
        return self._lado1

    @lado1.setter
    def lado1(self, lado1):
        self._lado1 = lado1

    @property
    def lado2(self):
        return self._lado2

    @lado2.setter
    def lado2(self, lado2):
        self._lado2 = lado2

    @property
    def lado3(self):
        return self._lado3

    @lado3.setter
    def lado3(self, lado3):
        self._lado3 = lado3

    @property
    def lado4(self):
        return self._lado4

    @lado4.setter
    def lado4(self, lado4):
        self._lado4 = lado4

    def calcArea(self):
        return self._base * self._altura

    def calcPerim(self):
        return self._lado1 + self._lado2 + self._lado3 + self._lado4


class Retangulo(Quadrilatero):
    __slots__ = [
        '_base','_altura'
    ]
    def __int__(self, base, altura):
        super(Retangulo, self).__int__(base, base, altura, altura)
        self.base = base
        self.altura = altura


    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    def calcArea(self):
        return self._base * self._altura

    def calcPerim(self):
        return self._lado1 + self._lado2 + self._lado3 + self._lado4

class Quadrado(Quadrilatero):
    __slots__ = ['_lado']

    def  __init__(self, lado):
        super(Quadrado, self).__init__(lado, lado, lado, lado)
        self.lado = lado

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, lado):
        self._lado = lado

    def calcArea(self, lado):
        return math.pow(self.lado, 2)

    def calcPerim(self, lado):
        return self._lado * 4

class Circulo:
    __slots__ = [
        '_raio'
    ]

    def __init__(self, raio):
        self.raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, raio):
        self._raio = raio

    def calcArea(self):
        return math.pi * math.pow(self._raio, 2)

    def calcPerim(self):
        return self._raio * 2 * math.pi


