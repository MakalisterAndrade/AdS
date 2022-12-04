from peewee import Model, OperationalError, CharField, IntegerField, ForeignKeyField,DateField,DecimalField
from playhouse.mysql_ext import MySQLConnectorDatabase


class BaseModel(Model):

    def __init__(self, *args, **kwargs):
        try:
            self.create_table()
        except OperationalError as erro:
            print(erro)

        super().__init__(*args, **kwargs)

    class Meta:
        database = MySQLConnectorDatabase('cbbd', user='root', password='',
                                          host='localhost', port=3306, charset='utf8mb4')



class Atividade(BaseModel):
    local = CharField(max_length=35)
    data = DateField()
    descricao = DecimalField()

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except OperationalError as e:
            print("Erro: " + e)

class Participante(BaseModel):
    nome = CharField(max_length=50, unique=True)
    instituicao = CharField(max_length=20, default='IFRO')
    endereco = CharField()
    telefone = CharField()
    email = CharField()
    categoria = CharField()
    atividade = ForeignKeyField(Atividade, related_name='descricao')

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except OperationalError as erro:
            print(str(erro))

class Revisor(BaseModel):

    nome = CharField(max_length=50, unique=True)
    instituicao = CharField(max_length=50, unique=True)

    rua = CharField(max_length=50, unique=True)
    numero = IntegerField()
    bairro = CharField(max_length=30, unique=True)
    cidade = CharField(max_length=50, unique=True)
    unidade_federativa = CharField(max_length=2, unique=True)


class Especialidade(BaseModel):

    nome = CharField(max_length=100, unique=True)
    revisor = ForeignKeyField(model=Revisor, on_delete="CASCADE", backref="especialidades")


class Contato(BaseModel):

    telefone = IntegerField()
    fax = IntegerField()
    revisor = ForeignKeyField(model=Revisor, on_delete="CASCADE", backref="especialidades")



class PalavrasChave(BaseModel):
    tags = CharField(max_length=100, unique=True)

class Artigo(BaseModel):

    titulo = CharField(max_length=100, unique=True)
    nome = CharField(max_length=100, unique=True)
    email = CharField(max_length=100, unique=True)
    palavras_chave = ForeignKeyField(model=PalavrasChave, on_delete='Cascade', backref='tags')


class Autor(BaseModel):
    pass


class Inscrito(BaseModel):
    pass


class Cientista(BaseModel):
    pass


class Local(BaseModel):
    pass


class Local_Atividade(BaseModel):
    capacidade = IntegerField()
    nome = CharField(max_length=100, unique=True)




class Sessao_Tecnica(BaseModel):
    descricao = CharField(max_length=100, unique=True)
    nome = CharField(max_length=100, unique=True)



class Palestra(BaseModel):
    titulo = CharField(max_length=100, unique=True)



class Minicurso(BaseModel):
    titulo = CharField(max_length=100, unique=True)
    descricao = CharField(max_length=100, unique=True)
    vaga_disponivel = bool(True)
    taxa = IntegerField()