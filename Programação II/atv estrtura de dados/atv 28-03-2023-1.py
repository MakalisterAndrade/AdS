"""
Makalister Andrade da Silva - UTF8 - 28/03/2022

Filtragem de dados


from calendar import c
from traceback import print_tb


def epar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


numeros = [4, 3, 8, 9, 12, 15, 16, 21]

# filtra números pares da lista

print(list(filter(epar, numeros)))


numeros = [4, 3, 8, 9, 12, 15, 16, 21]

print(list(filter(lambda nr: nr % 2 == 0, numeros)))


nomes = ['Elizangela', 'Maria', 'Ana', 'Laís']

print()
print(f'Nomes com menos de 5 caracteres')

lista_1 = list(map(lambda nome: {nome}, filter(lambda nome: len(nome) <5, nomes)))
print(lista_1)

print()
print('ou')
print()

print(f'Nomes com menos de 5 carcteres:', list(map(lambda nome: {nome}, filter(lambda nome: len(nome) <5, nomes))))


# Função all()

print(all([0, 1, 2, 3, 4]))

#Any()
print(any([0, 1, 2, 3, 4]))

#Type()
a = 5
print(type(a))

b = 'Olá Mundo!'
print(type(b))

c = True
print(type(c))

d = 0.50
print(type(d))

f = print
print(type(f))

g = []
print(type(g))

h = {}
print(type(h))

def funcao():
    pass
print(type(funcao))

# Type
"""
"""
lista = ["a", ["b", "c", "d"], "e"]

for x in lista:
    if type (x) is str:
        print(x)
    else:
        print(f"Lista: ", end="")
        for z in x:
            print(f" {z}", end="")
        print()

#type

def imprime_elementos(l, nivel=0):
    espacos = " "* 1 * nivel
    if type(l) == list:
        print(espacos, "[")
        for e in l:
            imprime_elementos(e, nivel + 1)
        print(espacos, "]")
    else:
        print(espacos, l)


L = [1,[2, 3, 4, [5, 6, 7]]]

imprime_elementos(L)


from traceback import print_tb
import types

a = (10, 15, 'IFRO')

print(isinstance(a, str))

print(isinstance(a, int))

print(isinstance(a, float))

print(isinstance(a, bool))

print(isinstance(a, list))

print(isinstance(a, tuple))

print(isinstance(a, set))

print(isinstance(a, dict))

print(isinstance(a, types.FunctionType))

print(isinstance(a, types.BuiltinFunctionType))
"""