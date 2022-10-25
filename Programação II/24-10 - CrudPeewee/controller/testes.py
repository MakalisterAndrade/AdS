from TurmaCtrl import TurmaCtrl

control = TurmaCtrl()
"""
texto = control.salvar_atualizar('3º ADS - 2022','Noturno')
print(texto)
"""

"""
texto = control.excluirTurma(2)
print(texto)
"""

turma = control.buscarTodasTurmas()

print(turma)