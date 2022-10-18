from turmaModel import Turma
class Aluno:
    """
    Classe base de alunos da Turma
    """
    __slots__=(
        '_id','_nome','_matricula','_cpf','_dataNasc','_turma'
    )

    def __int__(self, id=None, nome="", matricula=str, cpf=str, dataNasc=str, turma=''):
        self.id = id
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.dataNasc = dataNasc
        self.turma = Turma.id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matrticula(self, matricula):
        self._matricula = matricula

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def dataNasc(self):
        return self._dataNasc

    @dataNasc.setter
    def dataNasc(self, dataNasc):
        self._dataNasc = dataNasc

    @property
    def turma(self):
        return self._turma

    @turma.setter
    def turma(self, turma):
        self._turma = turma
