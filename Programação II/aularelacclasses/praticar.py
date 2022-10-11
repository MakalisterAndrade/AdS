class Livro:
    __slots__ = [
        '_titulo','_autores','_area', '_editora','_numero_f','_emprestado'
    ]

    def __init__(self, titulo,autores,area,editora,numero_f,emprestado = False):
        self.titulo = titulo
        self.autores = autores
        self.area = area
        self.editora = editora
        self.numero_f = numero_f
        self.emprestado = False

        @property
        def titulo(self):
            return self._titulo

        @titulo.setter
        def titulo(self, titulo):
            self._titulo = titulo

        @property
        def autores(self):
            return self._autores

        @autores.setter
        def autores(self, autores):
            self._autores = autores