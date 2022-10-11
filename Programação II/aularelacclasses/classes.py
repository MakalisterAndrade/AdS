"""
Makalister Andrade da Silva - UTF8

"""
class Conta():
    # Dessa forma, não é possível criar atr. dinamicamente

    __slots__ = {'_numero',
                 '_titular',
                 '_saldo',
                 '_limite'}

    def __init__(self, titular='', numero='', limite='', saldo=0.0):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo
        self.limite = limite

    # Encapsulamento
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, nome):
        self._titular = ''
        if len(nome) >= 5:
            self._titular = nome

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, novolimite):
        self._limite = novolimite

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor

    @saldo.setter
    def saldo(self, saldo):
        if hasattr(self, 'saldo'):
            if self._saldo == 0.00:
                self._saldo = saldo
            else:
                self._saldo = saldo

    def saque(self, valor):
        if valor <= (self.saldo + self.limite):
            self.saldo -= valor
            if self.saldo < 0:
                self.limite = self.limite + self.saldo
                self.saldo = 0.00
            return True
        return False
