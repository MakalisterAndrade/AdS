"""
Makalister Andrade da Silva UTF8 15/08/2022
"""
'''
Crie uma classe chamada Livro com os seguintes atributos: titulo, autor, páginas, preço.
Encapsule estes atributos (utilize todas as técnicas aprendidas).
O método setter de "preco" não deve permitir que seja definido um valor negativo para o preço do livro.
'''


class Livro():
    __slots__ = {'_titular',
                 '_autor',
                 '_paginas',
                 '_preco'}

    def __init__(self, titulo='', autor='', paginas='', preco=0.00):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.preco = preco


    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo


    @property
    def autor(self, ):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def paginas(self, ):
        return self._paginas

    @paginas.setter
    def paginas(self, paginas):
        self._paginas = paginas

    @property
    def preco(self, ):
        return self._preco


    @preco.setter
    def preco(self, preco):
        self._preco = ''
        if preco > 0:
           self._preco = preco
           print(f'Só são válidos inteiros reais')
