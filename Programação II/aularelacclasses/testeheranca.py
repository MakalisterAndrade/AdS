from heranca import Gerente,Programador,Funcionario

g = Gerente('Fulano de total', '12/05/1998', 2323.43, 'Projeto 1')

print(g.nome)
print(g.projeto)
f = Funcionario('Babel', '15-08-1997', 313.45)
prog = Programador('Jojo', '10-07-1998', 3223.33, 'Python')
#print(dir(prog))
print(prog.linguagem)

print('=' * 90)

print(Funcionario)

print()
print(f)
print(g)
print()
print('=' * 90)
print(g.calcIdade())