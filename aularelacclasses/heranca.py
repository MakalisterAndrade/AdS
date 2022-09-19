"""Makalister Andrade da Silva - UTF8 - 29/08/22"""
import math
from datetime import date


class Funcionario:
    __slots__ = [
        '_nome',
        '_nasc',
        '_salario'
    ]

    def __init__(self, nome='', nasc='', salario=0.00):
        self.nome = nome
        self.nasc = nasc
        self.salario = salario


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def nasc(self):
        return self._nasc

    @nasc.setter
    def nasc(self, nasc):
        self._nasc = nasc

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario



    def __str__(self):
        return f'Funcionário: {self._nome}'


class Gerente(Funcionario): # Gerente recebe todos os dados de Funcionário
    __slots__ = [
        '_projeto'
    ]
    def __init__(self, nome = '', nasc = '', salario = 0.00, projeto = ''):
# Primeira forma de chamar o construtor da super classe
#       Funcionario.__init__(self, nome, nasc, salario)
# Segunda forma...
#       super().__init__(nome, nasc, salario)
#Terceira forma...
        super(Gerente, self).__init__(nome, nasc, salario)
        self.projeto = projeto

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, projeto):
        self._projeto = projeto

    def __str__(self):
        return f'Gerente: {self._nome}'

    def calcIdade(self):
        nasc_list = self._nasc.split('/')
        nasc_int = int(nasc_list[2] + nasc_list[1] + nasc_list[0])
        hoje = date.today()
        data_atual = str(hoje).split('-')
        data_atual_int = int(data_atual[0] + data_atual[1] + data_atual[2])
        idade = math.floor((data_atual_int - nasc_int)/10000)
        return idade

class Programador(Funcionario):

    __slots__ = [
        '_linguagem'
    ]
    def __init__(self, nome, nasc, salario, linguagem):
        super(Programador, self).__init__(nome, nasc, salario)
        self._linguagem = linguagem

    @property
    def linguagem(self):
        return self._linguagem

    @linguagem.setter
    def linguagem(self, linguagem):
        self._linguagem = linguagem