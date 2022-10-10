"""
Makalister Andrade UTF8 - 22-08-2022

"""

class Editora:
    __slots__ = [
       '__codEditora',
        '__razaoSocial',
        '__contato',
        '__telefone'
    ]

    def __init__(self, codEditora=0, razaoSocial='', contato='', telefone=''):
        self.codEditora = codEditora
        self.razaoSocial = razaoSocial
        self.contato = contato
        self.telefone = telefone

    @property
    def codEditora(self):
        return self.__codEditora

    @codEditora.setter
    def codEditora(self, codEditora):
        self.__codEditora = codEditora

    @property
    def razaoSocial(self):
        return self.__razaoSocial

    @razaoSocial.setter
    def razaoSocial(self, razaoSocial):
        self.__razaoSocial = razaoSocial

    @property
    def contato(self):
        return self.__contato

    @contato.setter
    def contato(self, contato):
        self.__contato = contato

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone


class Livro:
    __slots__ = [
        '__editora',
        '__codigo',
        '__descLivro',
        '__isbn'
    ]


    def __init__(self, editora=None, codigo=0, descLivro='', isbn='',):
        self.editora = editora
        self.codigo = codigo
        self.descLivro = descLivro
        self.isbn = isbn


    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descLivro(self):
        return self.__descLivro

    @descLivro.setter
    def descLivro(self, descLivro):
        self.__descLivro = descLivro

    @property
    def isbn(self):
        return self.isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = editora
        else:
            self.__editora = None
            return 'Não foi dessa vez meu chapa'





