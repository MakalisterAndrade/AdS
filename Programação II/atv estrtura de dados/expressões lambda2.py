"""
Makalister Andrade da Silva - UTF8 - 21-03-2022

Expressões lambdas

calcula = lambda x: 3* x + 1

print(calcula(7))

# Linha 6 guarda a função lambda dentro da variavel 'calcula'
# com parametro 'x' e uma expressão matematica
# Linha 7 printa a variavel(que chama a função) na tela dando a 'x' o valor '7'

aumento = lambda a, b: (a * b / 100)
print(aumento(100, 5))

# Linha 14 Guarda a função lambda com parametros 'a' e 'b'
# dentro da variavel 'aumento'
# Linha 15 printa na tela, chamando a variavel(que chama a função lambda)
# Dando os argumentos '100' e '5' aos parametros

academico_curso = lambda academico, curso: academico.strip().title() +' '+ curso.strip().title()
print(academico_curso('Gerimunda ',' das Dores'))
print(academico_curso(' instituto federal ', ' campus ariquemes, Análise e Desenvolvimento de Sistemas'))

#Linha 22 guarda na variavel a lambda que aplica um tratamento aos parametros que serão dados
#strip() e title() transformam a primeira letra das string em maiúscula, o metódo de separação para a procura dos argumentos é o 'espaço'
#Linhas 23 e 24 printam a variavel que chama lambda passando os argumentos 
"""

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
    return lambda x: a * x ** 2 + b *x + c


quadratica = funcao_quadratica(2, 3, -5)


print(quadratica(0))
print(quadratica(1))
print(quadratica(2))

# 1) Desenvolvimento 1

from _functools import reduce

distancias = [44, 45, 32, 47, 21]
lamb = lambda x: 5.50 + 2.50*x

def calc(x):
    return 5.50 + 2.50*x


def soma(a, b):
    return a + b

tot = list(map(calc, distancias))



print(f'A distância de cada corrida percorrida no dia foi de: {distancias}')
print()
print(f'O valor de cada corrida percorrida no dia foi de:  {tot}')
print()
print(f'O faturamento do dia foi de: R${reduce(soma, tot):.0f},00')
print()



# 2) Refatore o desenvolvimento 1, usando expressão lambda;

print(f'A distância de cada corrida percorrida no dia foi de: {distancias}')
print()
#print(f'O valor de cada corrida percorrida no dia foi de:  {list(map(lamb, distancias))}')
#print()
print(f'O valor de cada corrida percorrida no dia foi de:  {list(map(lambda x: 5.50 + 2.50*x, distancias))}')
print()
print(f'O faturamento do dia foi de: R${reduce(soma, list(map(lambda x: 5.50 + 2.50*x, distancias))):.0f},00')
print()

#3) Refatore usando lambda com listas multiplas

dist_1, dist_2, dist_3 = [10, 20, 30, 40, 50],  [1, 2, 3, 4, 5], [11, 22, 33, 44, 55]

print(f'A distância de cada corrida percorrida no dia foi de: {list(map(lambda x, y, z: x+y+z, dist_1, dist_2, dist_3))}')
print()
print(f'O valor de cada corrida percorrida no dia foi de:  {list(map(lambda x, y, z: (x+y+z)*2.50 + 5.50, dist_1, dist_2, dist_3))}')
print()
print(f'O faturamento do dia foi de: R$ {reduce(soma, list(map(lambda x, y, z: (x+y+z)*2.50 + 5.50, dist_1, dist_2, dist_3))):.1f}')

#4) Desenvolva um script que calcule a temperatura em graus Fahrenheit, usando lambda

#cidades = [('São Paulo',29), ('Porto Velho', 36), ('Cuiabá', 19), ('Curitiba', 26), ('Brasília', 27), ('Tocantins', 38), ('Macapá', 40)]
print()
#print(f'A temperatura em Fahreinheit é: {map(list(lambda y, c: 9 * c / 5 + 32, cidades))}')
cidades = lambda cit, c: print (f'Cidade {cit}; Graus Fahreinheit {9 * c / 5 + 32}')
cidades('São Paulo',29), ('Porto Velho', 36), ('Cuiabá', 19), ('Curitiba', 26), ('Brasília', 27), ('Tocantins', 38), ('Macapá', 40)
print()

#5) Desenvolva um script que calcule subtração dos elementos de uma lista, que apresente diretamente na tela o resultado

valors = [780, 457, 50, 12, 88]
print(f'Subtração final dos valores {valors} é igual a {reduce(lambda x, b: x - b, valors)}')

"""
