class Imobiliaria:
    __slots__ = ['_quantidade','_imoveis']

    def __init__(self, quantidade = int):
        self._imoveis = Imovel()
        self._quantidade = quantidade

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade


    def inserir(self):
        pass


    def remover(self):
        pass


    def alugar(self):
        pass

    def devolver(self):
        pass

    def Quantidade(self):
        pass

    def listarImoveis(self):
        pass

class Imovel:
    __slots__ = ['_codigo','_regiao','_area','_disponivel']

    def __init__(self, codigo=0, regiao = '', area = 0, disponivel=False):
       self._codigo = codigo
       self._regiao = regiao
       self._area = area
       self._disponivel = disponivel

    @property






'''
        def __eq__(self, other):

            if self.codigo == other.codigo and self.regiao == other.regiao and self.disponivel == other.disponivel:

                return true

            else:

                return false
'''