class Aluno:
    """
    Classe base de alunos da Turma
    """
    __slots__=(
        '_id','_nome','_matricula','_cpf','_dataNasc'
    )

    def __int__(self, id=None, nome="", matricula=int, cpf=int, dataNasc=None):
        self.id = id
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.dataNasc = dataNasc