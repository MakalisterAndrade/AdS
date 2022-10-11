from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    """
    Qualquer classe que herdar dessa, deve implementar todos
    os métodos da classe.
    """
    @abstractmethod
    def calcula_perimetro(self):
        """calcula o perímetro de uma forma geométrica"""
        pass

    @abstractmethod
    def calcula_area(self):
        """calcula a área da forma geométrica"""
        pass


class Quadrilatero(FormaGeometrica):
    __slots__ = ('_lado1',
                 '_lado2',
                 '_lado3',
                 '_lado4',)

    def __init__(self, lado1, lado2, lado3, lado4):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado4 = lado4

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

    def calcula_perimetro(self):
        return self._lado1 + self._lado2 + self._lado3 + self._lado4

    @abstractmethod
    def calcula_area(self):
        pass


class Retangulo(Quadrilatero):
    __slots__ = ('__base',
                 '__altura',)

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        super().__init__(base, altura,base, altura)

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base):
        self.__base = base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def calcula_area(self):
        return self.__base * self.__altura


class Quadrado(Quadrilatero):
    __slots__ = ('__lado',)

    def __init__(self, lado):
        super().__init__(lado, lado, lado, lado)
        self.lado = lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, lado):
        self.__lado = lado

    def calcula_area(self):
        return self.__lado ** 2


class Circulo(FormaGeometrica):
    PI = 3.1415
    __slots__ = ('__raio',)

    def __init__(self, raio):
        self.raio = raio

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, raio):
        self.__raio = raio

    def calcula_perimetro(self):
        return 2 * self.PI * self.__raio

    def calcula_area(self):
        return self.PI * (self.__raio ** 2)
    