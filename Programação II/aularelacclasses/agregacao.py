import time
from time import sleep

class Produto:
    __slots__ = [
        '_codigo',
        '_descProd',
        '_preco',
        '_quantidade'
    ]

    def __init__(self, codigo=0, descProd='', preco=0.00, quantidade=0):
        self.codigo = codigo
        self.descProd = descProd
        self.preco = preco
        self.quantidade = quantidade

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def descProd(self):
        return self._descProd

    @descProd.setter
    def descProd(self, descProd):
        self._descProd = descProd

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    def mostraDados(self):
        time.sleep(0.2)
        print(f' Código do Produto: {self._codigo} Descrição: {self._descProd} Preço: {self._preco} Quantidade: {self._quantidade}')

class Carrinho:
    __slots__ = [
        '_itens'
    ]

    def __init__(self):
        self._itens = []

    @property
    def itens(self):
        return self._itens

    @itens.setter
    def itens(self, itens):
        self._itens.append(itens)

    def exibeCarrinho(self):
        for i in self._itens:
            i.mostraDados()

    def fecharCompra(self):
        total = 0.00
        for i in self._itens:
            total += i.preco
            i.quantidade -= 1
        self.exibeCarrinho()
        print(f'Total da compra: R$ {total:.2f}')
        #tot = round(total)
        #rint(f'Total da compra: R$ {tot:.2f}')
