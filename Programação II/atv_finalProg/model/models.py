import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase


class BaseModel(peewee.Model):

    class Meta:
        database = MySQLConnectorDatabase('bdfinal', user='root', password='',
                                           host='localhost', port=3306, charset='utf8mb4')

class Atividade(BaseModel):
    local = peewee.CharField(max_length=35)
    data = peewee.DateField()
    descricao = peewee.DecimalField()

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as e:
            print("Erro: " + e)

class Participante(BaseModel):
    nome = peewee.CharField(max_length=50, unique=True)
    instituicao = peewee.CharField(max_length=20, default='IFRO')
    endereco = peewee.CharField()
    telefone = peewee.CharField()
    email = peewee.CharField()
    categoria = peewee.CharField()
    atividade = peewee.ForeignKeyField(Atividade, related_name='descricao')

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as erro:
            print(str(erro))
