"""
Makalister Andrade da Silva - UTF8 - 21-03-2022

Expressões lambdas

calcula =lambda x: 3* x + 1

print(calcula(7))


aumento = lambda a, b: (a * b / 100)
print(aumento(100, 5))


academico_curso = lambda academico, curso: academico.strip().title() +' '+ curso.strip().title()
print(academico_curso('Gerimunda ',' das Dores'))
print(academico_curso(' instituto federal ', ' campus ariquemes, Análise e Desenvolvimento de Sistemas'))


#Expressões lambda com nenhuma ou várias entradas
#Lambda sem entrada e com um retorno

sem = lambda:'Python é uma linguagem dinâmica'
uma = lambda x: 4 * x + 1
duas = lambda x, y: (x * y) ** 1.8
tres = lambda x, y,z: 4 / (2 / x + 2 / y + 3/ z)


lista_1 = ['A', 'D', 'C', 'E', 'd',]
lista_1.sort(key = lambda k: k.lower())
print(lista_1)


atrizes = ['Ingrid Bergman',
            'Vivien Leigh',
            'Audrey Hepburn',
            'Sophia Loren',
            'Ann MArget',
            'Marlene Dietrich', 'Elizabeth Taylor', 'Greta Garbo']

atrizes.sort(key=lambda nome: nome.split(' ') [0].lower())
print(atrizes)


#Funções quadráticas

def funcao_quadratica(a, b, c):
"""

from ntpath import join


distancias = [120, 100, 50, 70, 88]

print( 'A distâncias de cada corrida percorrida no dia foi de: ', end="")
for e in list(map(lambda x: 5.50 + 2.50*x, distancias)) : print(e, end=" ")