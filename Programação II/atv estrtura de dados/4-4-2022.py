"""
Makalister Andrade da Silva 4-4-2022 - UTF8

 # Iteravel
nome = 'IFRO Campus Ariquemes' # é um iteravel, mas nao um interador.


numeros = [1, 2, 3, 4, 5, 6] # é um iterável, mas não é um interator. 

#Iterador : Em Python a função iter(), cria um iterador.
lista_1 =[11, 22, 33, 95] #lista_1 = iteravel

lista_i = iter(lista_1) # lista_i = iterador

print(lista_i)

print(next(lista_i))
print(next(lista_i))
print(next(lista_i))
print(next(lista_i))
print(next(lista_i))
"""

# 03 - Iterator com for 

nome = 'IFRO'

for letra in nome: 
    print(f'{letra}') 

# 04 - Loop comum - com lista

for num in [8, 3, 9, 16, 87]: 
    print(num) 

# 05 - Por dentro da função for()
def dentro_do_for(interavel):
    it = iter(interavel)
    while True:
        try: # tente executar o bloco abaixo 
           print(next(it))
        except StopIteration: # senão execute o bloco abaixo
            break
dentro_do_for(([80, 30, 90, 160, 89]))

# 06  Generator function

def contando(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador # fica aguardando um next
        contador = contador + 1

numeros = contando(4)

print(type(numeros))
print()

print(next(numeros))
print(next(numeros))
print(next(numeros))
print(next(numeros))
print()

numeros = list(contando(5))
print(type(numeros))
print(numeros)

# 07 - Função de Fibonacci com listas e função for()

def fib_lista(max):
    nums = []
    a,b = 0, 1 
    while len(nums) < max:
        nums.append(b)
        a,b = b, a+b
    return nums


for n in fib_lista(100):
    print(n)


# Função de Fibonacci com generator e função for()

def fib_gerador(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a,b=b, a+b
        yield a
        contador = contador + 1

for n in fib_gerador(100):
    print(n)


# 09 generators comuns

def numeros():
    for num in range(1, 10):
        yield num

numeros_gerados = numeros()

print(numeros_gerados)
print()

print(next(numeros_gerados))
print(next(numeros_gerados))


#10 - Generator Comprehensions
nomes = ['Claudinei', 'Carla', 'Camila', 'Cristiane', 'Vanessa']

resultado = (nome[0] == 'C' for nome in nomes)
print(type(resultado))
print(resultado)
print(tuple(resultado))
print()

print(any(nome[0] == 'C' for nome in nomes))


#11 - Generator Comprehensions

numeros_gerados_2 = (num for num in range(1, 10))
print(numeros_gerados_2)
print()

print(next(numeros_gerados_2))
print(next(numeros_gerados_2))

print()
print(list(numeros_gerados_2))


# 12 retorna a quantidade de bytes em memoria

from sys import getsizeof

print(getsizeof('INSTITUTO'), ": bytes")
print()

print(getsizeof('FEDERAL'), ": bytes")
print()

print(getsizeof(5), ": bytes")
print()

print(getsizeof(51), ": bytes")
print()

print(getsizeof(151005), ": bytes")
print()

print(getsizeof(True), ": bytes")
print()