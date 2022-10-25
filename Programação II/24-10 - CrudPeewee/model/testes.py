from model.models import Turma, Aluno
"""
turma = Turma()
turma.nome = '3º ADS'
turma.turno = 'Noturno'
turma.save()
"""
"""
aluno = Aluno()
aluno.nome = 'Siclano de tal'
aluno.dt_nasc = '2100-11-05'
aluno.renda_fam = 2100.12
aluno.turma = Turma.get_by_id(1)

aluno.save()
"""

aluno = Aluno.get(nome='Siclano de tal') # buscar o valor(id) da da coluna aluno pelo nome
print(aluno)
print(aluno, aluno.dt_nasc, aluno.turma, aluno.turma.nome)

colegas = aluno.turma.alunos #  usando o backref para buscar todos os valores da coluna
for c in colegas:
    print (c.nome)