import time


class Produto:
    __slots__ = ['_cod','_descricao','_marca','_valor','_estoque']

    def __init__(self,cod,descricao,marca,valor,estoque):
        self.cod = cod
        self.descricao = descricao
        self.marca = marca
        self.valor = valor
        self.estoque = estoque

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

    @property
    def estoque(self):
        return self._estoque

    #Não deve existir o método setEstoque, em seu lugar devem existir os métodos: aumentaEstoque(quant) e reduzEstoque(quant). 
    def aumentaEstoque(self,quant):
        if quant > 0:
            self._estoque += quant

    def reduzEstoque(self,quant): #Fazer verificação, pra não ficar negativo.
        if quant < self._estoque | quant > 0:
            self._estoque -= quant
            return True
        return False


    def mostraDados(self):
        time.sleep(0.2)
        print(f' Código do Produto: {self._cod} Descrição: {self._descricao} Preço: {self._valor} Quantidade: {self._marca}')


"""
b-  Crie uma classe chamada Item que contenha os atributos: numero, quant (unidades do pedido), produto (produto do qual o item faz parte). 
Encapsule os atributos. Crie um construtor com todos os atributos."""

class Item:
    __slots__ = ['_numero','_quant','_produto']

    def __init__(self, numero, quant, produto: Produto):
        self.numero = numero
        self.quant = quant
        self.produto = produto

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

    @property
    def produto(self):
        return self._produto

    @produto.setter
    def produto(self, produto):
        self._produto = None
        if isinstance(produto, Produto):
            self._produto = produto

"""
c- Crie uma classe chamada Pedido que contenha os atributos: numero, total, itens (vetor de itens), encapsule corretamente os atributos. 
Não deve existir o método “setTotal”, o total será incrementado sempre que for inserido um item. 
O método setItens deve ser criado de forma que seja adicionado um item de cada vez."""


class Pedido:
    __slots__ = [ '_numero', '_total','_itens', '_cliente']

    def __init__(self, numero, cliente: 'Cliente'):
        self.numero = numero
        self._total = 0
        self._itens = []
        self.cliente = cliente

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = None
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    @property
    def itens(self):
        return self._itens

    @property
    def total(self):
        return self._total

    @itens.setter
    def itens(self, item:  Item):
        self.itens.append(item)
        self._total += (item.produto.valor * item.quant)


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