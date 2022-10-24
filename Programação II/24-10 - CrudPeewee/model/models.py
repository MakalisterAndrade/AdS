import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase

class BaseModel(peewee.Model): #Herda do peewee ferramentas e packs para cone]ao com o banco
    class Meta: #claase meta, subclasse para realizar conexão
        database = MySQLConnectorDatabase(
            'escolapeewee',
            user='root',
            password='',
            port='3306',
            charset='utf8mb4' #Não obrigatório, boa prática para definir os caracteres aceitos no banco
        )
class Turma(BaseModel):
    nome = peewee.CharField(100, unique=True)#Criação do atributo, a tabela no banco de dados
    turno = peewee.CharField(20, null=True, choices=('Matutino',
                                                     'Vespertino', 'Noturno', 'Integral'))#Criação do atributo, a tabela no banco de dados
    def __init__(self, *args, **kwargs):
        try:
            self.create_table()
        except peewee.OperationalError as erro:
            print(str(erro))
            #return erro
        super.__init__(*args, **kwargs)

