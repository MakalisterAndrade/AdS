import time


class Produto:
    __slots__ = ['_cod','_descricao','_marca','_valor','_estoque']

    def __init__(self,cod,descricao,marca,valor,estoque=0):
        self._cod = cod
        self.descricao = descricao
        self.marca = marca
        self._valor = valor
        self._estoque = estoque

    @property
    def cod(self):
        return self._cod

    @cod.setter
    def cod(self,cod):
        self._cod = cod

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self,desc):
        self._descricao = desc

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self,valor):
        self._valor = valor

    #Não deve existir o método setEstoque, em seu lugar devem existir os métodos: aumentaEstoque(quant) e reduzEstoque(quant). 
    def aumentaEstoque(self,quant):
        estoqueTotal = self._estoque + quant
        return estoqueTotal

    def reduzEstoque(self,quant): #Fazer verificação, pra não ficar negativo.
        estoqueTotal = self._estoque - quant
        return estoqueTotal

    def mostraDados(self):
        time.sleep(0.2)
        print(f' Código do Produto: {self._cod} Descrição: {self._descricao} Preço: {self._valor} Quantidade: {self._marca}')


"""
b-  Crie uma classe chamada Item que contenha os atributos: numero, quant (unidades do pedido), produto (produto do qual o item faz parte). 
Encapsule os atributos. Crie um construtor com todos os atributos."""

class Item(Produto):
    __slots__ = ['_numero','_quant']

    def __init__(self, cod, descricao, marca, valor, estoque, numero,quant):
        super().__init__(cod, descricao, marca, valor, estoque)
        self.numero = numero
        self.quant = quant

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self,numero):
        self._numero = numero

    @property
    def quant(self):
        return self._quant

    @quant.setter
    def quant(self,quant):
        self._quant = quant

"""
c- Crie uma classe chamada Pedido que contenha os atributos: numero, total, itens (vetor de itens), encapsule corretamente os atributos. 
Não deve existir o método “setTotal”, o total será incrementado sempre que for inserido um item. 
O método setItens deve ser criado de forma que seja adicionado um item de cada vez."""


class Pedido():
    __slots__ = [ '_total', '_itens', '_cliente']

    def __init__(self, total):
        self._total = total
        self._itens = []
        self._cliente = Cliente()


    @property
    def itens(self):
        return self._itens

    @itens.setter
    def itens(self, itens):
        self._itens.append(itens)


    def mostraPed(self):
        for i in self._itens:
            i.mostraDados()
            total = 0.00
            for i in self._itens:
                total += i.valor
                i.quant -= 1
            self.mostraPed()
            print(f'Total da compra: R$ {total:.2f}')


"""
d – Crie uma classe Cliente com os atributos: nome, CPF e telefone. 
Encapsule os atributos e crie um construtor com todos os atributos."""

class Cliente:
    __slots__ = ['_nome','_cpf','_telefone']

    def __init__(self,nome='',cpf='',telefone=''):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self,cpf):
        self._cpf = cpf

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self,telefone):
        self._telefone = telefone

"""
f - Altere classe Pedido e adicione um relacionamento
de associação (agregação) para a classe Cliente (acrescentar atributo cliente). 
Não esqueça de encapsular."""

"""
g- Teste a classe pedido.

"""