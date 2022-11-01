import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase

class BaseModel(peewee.Model): #Herda do peewee ferramentas e packs para cone]ao com o banco
    def __init__(self, *args, **kwargs):
        try:
            self.create_table()
        except peewee.OperationalError as erro:
            print(erro)
        super().__init__(*args, **kwargs)

    class Meta: #claase meta, subclasse para realizar conexão
        database = MySQLConnectorDatabase(
            'escolapeewee',
            user='root',
            password='root',
            port='3306',
            charset='utf8mb4' #Não obrigatório, boa prática para definir os caracteres aceitos no banco
        )

class Turma(BaseModel):
    nome = peewee.CharField(100, unique=True)#Criação do atributo, a tabela no banco de dados
    turno = peewee.CharField(20, null=True, choices=('Matutino',
                                                     'Vespertino', 'Noturno', 'Integral'))#Criação do atributo, a tabela no banco de dados
"""    
    def __init__(self, *args, **kwargs):
        try:
            self.create_table()
        except peewee.OperationalError as erro:
            print(str(erro))
            #return erro
        super.__init__(*args, **kwargs)
"""
class Aluno(BaseModel):
    nome = peewee.CharField(100)
    dt_nasc = peewee.DateField()
    renda_fam = peewee.DecimalField(max_digits=12, decimal_places=2)
    turma = peewee.ForeignKeyField(Turma, on_delete='CASCADE',
                                   backref='alunos')# vincula aluno(table) a aluno(table), ChaveEstrangeira
    #backref, através dele eu puxo outros atributos da mesma tabela
