"""
Makalister Andrade da Silva - UTF8
Abstração e atributos de classe 08-08-2022
"""
'''
1. Identifique as classes com os seus atributos 
(classes de análise/domínio) para os seguintes contextos:

a. Numa turma de um curso de graduação, temos disciplinas ministradas em salas
diferentes.

class classe:
    def __init__ (self, data_i, periodo, turno):
        self.data_i = data_i
        self.periodo = periodo
        self.turno = turno

class disciplinas:
    def disciplina(self, programacao, redes, ingles):
        self.programacao = programacao
        self.redes = redes
        self.ingles = ingles

class curso:
    def id(self, ads, bio, agro):
        self.ads = ads
        self.bio = bio
        self.agro = agro

class sala:
    def salas(self, lugares, andar, bloco, numero):
        self.lugares = lugares
        self.andar = andar
        self.bloco = bloco
        self.numero = numero
'''

'''
b. Está passando na rede de cinemas ArtFilme o filme “Jogos 2”, todos os dias,
em três sessões diárias.
Aos sábados e domingos existem em algumas sessões duas salas de exibição.


class datas:
    def dat (self, seg, ter, qua, qui, sex, sab, dom, horarios):
        self.seg = seg
        self.ter = ter
        self.qua = qua
        self.qui = qui
        self.sex = sex
        self.sab = sab
        self.dom = dom
        self.horarios = horarios

class filme:
    def descricao(self, nome, genero, indicacao):
        self.nome = nome
        self.genero = genero
        self.indicacao = indicacao

class salas:
    def sal(self, numero, lugares, tipo):
        self.numero = numero
        self.lugares = lugares
        self.tipo = tipo

class cinema:
    def cici(self, nome, local, telefone):
        self.nome = nome
        self.local = local
        self.telefone = telefone


'''
'''
2. Se dois desenvolvedores modelarem uma mesma classe X
para sistemas distintos,obrigatoriamente as classes terão
os mesmos atributos e operações? Por que?
R. Não, pois cada sistema tem suas próprias características e a definiçã
 de suas classes e atributos variam de acordo com seus aspectos próprios.
'''
'''
3. Identifique os atributos para as classes a seguir:

a. Conta-corrente:
R. numero, agência, tipo da conta, saldo, extrato, senha, cpf...

b. Caderno vendido em papelaria:
R. numero de folhas, quantidade de matérias, tamanho, tipo da capa, preço...

c. Arquivo de computador:
R. nome, tamanho, data de criação, permições do usuaŕio...

'''