class Revistas:
    def __init__(self, codigo=0, titulo='', tipo='', edicao=None):
        self.codigo = codigo
        self.titulo = titulo
        self.tipo = tipo
        self.edicao = Edicao()

    def setEdicao(self, numEdicao:int, dataEdicao, numArtigos: int):
        self.edicao.setEdicao(numEdicao, dataEdicao,numArtigos)

    def getEdicao(self):
        return self.edicao

class Edicao:

    def setEdicao(self, numEdicao, dataEdicao, numArtigos):
        self.numEdicao = numEdicao
        self.dataEdicao = dataEdicao
        self.numArtigos = numArtigos

    def getEdicao(self):
        return self