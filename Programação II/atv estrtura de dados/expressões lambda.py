"""
Makalister Andrade da Silva - UTF8 - 21-03-2022



def funcao_1(x):
    return x + 1

print(funcao_1(9))


#Expressão lambda
funcao_1 = lambda x: x + 1

print(funcao_1(9))

# Expressão lambda com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + '' + sobrenome.strip().title()

print(nome_completo(' claudinei',' de oliveira'))
print(nome_completo('instituto federal de rondônia','- campus ariquemes'))

atores = ['Leonardo DiCaprio', 'Brad Pitt', 'Denzel Washington', 'Philip Seymour Hoffman', 'Will Smith', 'Johnny Depp']
atores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(atores)

#Funções Quadráticas
#8
def funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

quadratica = funcao_quadratica(2, 3, -5)


print(quadratica(0))
print(quadratica(1))
print(quadratica(2))

#9
def somar(x):
    funcao_2 = lambda x: x + 9
    return funcao_2(x) * 13

print (somar(4))

a = (lambda x: x*2)
print(a(4))

#Calcula a area de um circulo com raio r
import math
def area(r):
    return math.pi * (r ** 2)

raios = [4, 10, 14.2, 0.6, 20, 88]

#for() default
areas =[]
for r in raios:
    areas.append(area(r))

print(areas)

# Calcula a area de um circulo com raio r - aplicando map
import math 
def area(r):
    return math.pi * (r ** 2)

raios = [4, 10, 14.2, 0.6, 20, 88]

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))

print()
print(f'O valor de areas após a primeira execução de map() é: {list(areas)}')

import math
raios = [4, 10, 14.2, 0.6, 20, 88]
print(list(map(lambda r: math.pi * (r**2), raios)))



from _functools import reduce
lista = [1, 2, -3, 4, 5, -9]
def soma(a, b):
    return a + b

print(reduce(soma, lista))
"""