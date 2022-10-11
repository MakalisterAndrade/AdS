"""Makalister Andradade da Silva - UTF8 - 23-05-22
Arrays, listas simp encade. e modularização II
"""
#ARRAYS

# 01 - arrays - criando um array vazio

from array import array

numeros = array('i', [])  # 01 = Type code

print(numeros)
print(type(numeros))
print()

# 02 - arrays - Populando o array vazio

for i in range(5):
    temp = int(input(f'Digite o número do índice {i} da memória: '))
    numeros.append(temp)
print(numeros)
print(f'Valor do índice {3} do array populado: numeros [3]')

# 03 - array.itemsize: verificar o comprimento em bytes de um array.

print(f'O tamanho do array em bytes é: {numeros.itemsize}')

# 04 - array.typecode: retorna o typecode usado para criar o array.

print(f'O typecode usado para criar o array é: {numeros.typecode}')

# 05 - array. array.buffer_info(): Retorna uma tupla - fornecendo o endereço de
# memória atual e o comprimento em elementos do buffer usado para armazenar
# o conteúdo do array

print(f'O endereço de memória e o comprimento do array são: {numeros.buffer_info()}')

# 06 - array.count(): Retorna o número de vezes que um valor ocorre no array.

print(f'O número de vezes que o valor 2 ocorre no array é: {numeros.count(2)}')

"""
#  07 - array.fromfile(f, n): faz a leitura dos elementos do array (como valores
#de máquina - binário) e armazena esses elementos em um objeto de arquivo
#através do parâmetro f.

#O parâmentro n da função é onde determinamos o número de elementos
#que serão inseridos, se houve diferença entre o número de elementos um
#EOFError é gerado, porém os itens disponíveis serão inseridos. Observação:
#esse objeto não funciona com o método read()
"""
# 07.1 # 07.1 - array.fromfile(f, n): gravando e lendo números em um arquivo binário

numeros = array("f")

for i in range(5):
    numeros.append(float(input(f'Digite o valor do salario no indice {i} = R$: ')))
print()
print(f'Armazenados na memoria RAM de seu equipamento sao: {numeros}')

print(input('>>> Tecle " ENTER " para continuar <<<'))
print()

f = open("salarios.bin", "wb")
array("f", numeros).tofile(f)
print(f'ARMAZENADOS no arquido binario salarios.bin de seu equipamento sao: {numeros}')

f.close()

print(input('>>> Tecle " ENTER " para continuar <<<'))
print()

salario = array("f")
f = open("salarios.bin", "rb")
salario.fromfile(f, 5)
print(f'LIDOS no arquido binario salarios.bin de seu equipamento sao: {salario}')

print()
for i in range(len(salario)):
    valorSalario = f'R$ {salario[i]:_.2f}'
    valorSalario = valorSalario.replace('.', ',').replace('_', '.')
    print(f'Salário armazenado no indice: {i} é: {valorSalario}')
f.close()

# 07.2 - array .fromfile(f, n): gravando lendo string em um arquivo binário

from array import array

nomes = array('u')
for i in range(3):
    nomes.append(input(f'Digite o nome do que ficará armazenado no índice {i}: '))

print()
print(f'Armazenados na memória RAM de seu equipamento são: {nomes}')
print(input('>>> Tecle " ENTER " para continuar <<<'))
print()

f = open("academicos.bin", "wb")
array("u", nomes).tofile(f)
print(f'ARMAZENADOS no arquivo binario academicos.bin de seu equipamento: {nomes}')

f.close()
print(input('>>> Tecle " ENTER " para continuar <<<'))

matriculados = array("u")
f = open("academicos.bin", "rb")
matriculados.fromfile(f, 3)

print(f'LIDOS no arquivo binario academicos.bin de seu equipamento sao: {matriculados}')

print(input('>>> Tecle " ENTER " para continuar <<<'))
print()

# Atenção: o ‘u’ código de tipo é para caracteres individuais.

# 07.3 - aplicando for para imprimir os acadêmicos matriculados - por indice
print('Imprimindo acadêmicos matriculados por indice')
print()
for i in range(len(matriculados)):
    print(f'Imprimindo o indice: {i} do array matriculados: {matriculados[i]}')

# LISTAS SIMPLRESMENTE ENCADEADAS
# MODULARIZAÇAO II
# 1 - Importando todo o módulo - não recomendado
# Quando um módulo é importado dessa forma, todas funções,
# atributos, classes e propriedades ficarão disponíveis em memória para uso

# 1.1 - Importando todo o módulo - não recomendado]

import random

#O ideal é conhecer quais funções do existem no módulo
#randoM e quais são necessárias para ajudar a solucionar
#nosso problema.

# 1.1.1 - conhecendo as funções do random

print(dir(random))

# 1.1.2 - Como aplicar uma das fungdes do random?
print(help(random.random))

# 1.1.3 - Utilizando a função random do pacote random
print(random.random())

# 2 - Importando uma função específica do módulo random - recomendado
# 2.1 - Importando a função random do módulo random

from random import random
print('Imprimindo 5 números aleatórios')
print()
for i in range(5):
    print(random())

# Esse tipo de função é utilizado principalmente em inteligência
# artificial, redes neurais artificiais para gerar os valores dos pesos.

# 2.2 - Importando a função uniform do módulo random.
# A função uniform() gera números float aleatórios entre valores estabelecidos.

from random import uniform

print()

for i in range(10):
    print(uniform(5, 12))
print()

# 2.3 - Importando a função randint do módulo random
# A função randint() gera números inteiros aleatórios entre valores estabelecidos.

from random import randint

for i in range(15):
    print(randint(1, 26))
print()
# 2.3.1 - Apostas para a lotofácil - pode repetir números

from random import randint

# Apostas para a lotofácil
for i in range(15):
    print(randint(1, 26), end=',')

# 2.4 - Importando a função choice do módulo random

# A função choice() apresenta um valor aleatório entre um iterável
# Desenvolva um script que receba uma lista com 10 números e após
# use a função choice() para sortear um número Pode acontecer da
# função pode repetir números.

from random import choice

lista = [2,1,5,4,3,6,7,8,9,11,14,19,17,22,29]

print(f'O sorteado foi: {choice(lista)}')
print()

# 2.4.1 - Sorteio de um número - pode repetir números
from random import choice
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(f'O número sorteado foi: {choice(lista)}')

print()

# 2.5 - Importando a função shufle do módulo random
# A função shufle () embaralhar os dados passados
# 2.5.1 -Jogando cartas - embaralhando
from random import shuffle
print('Embaralhando cartas')

print()
baralho = ['1' 'K', '9' 'Q','8"J', 'A', '3','2', '5', '7','6', '6' ]
print(f'    Lista original de cartas: {baralho}')

print()
shuffle(baralho)
print(f'Lista de cartas embaralhadas: {baralho}')

print()
print(f'    Carta retirada do baralho: {baralho.pop()}')

# 3 - Utilizando alias - apelidos para a função

import random as rdm
print()
print(rdm.random())

# 4 - Importando todas as funções de um modulo:

from random import  *

print()

print(random())

# 5 - Importando todo o modulo
import random
print()
print(random.random())

# 6.1 - Múltiplos imports

from random import (random, randint, shuffle, choice) # Não Pythonica

from random import (
    random,
    randint,
    shuffle,
    choice) # Forma Pythonica

print(random())
print(randint(5, 15))
lista = ['IFRO', 'ADS', 'ESTRUTURA DE DADOS']
shuffle(lista)
print(lista)

# 7 - Utilizando alias para múltiplas funções:
from random import randint as rdi, random as rdm

print()

print(rdi(8, 89))

print()
print(rdm())