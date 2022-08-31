"""
Makalister Andrade da Silva - UTF 8 - 07-03-2022

def epar(x):
    return x % 2 == 0


def par_ou_impar(x):
    if epar(x):
        return "par"
    else:
        return "impar"


print(par_ou_impar(8))
print(par_ou_impar(15))


def pesquisa(lista, valor):
    for i, x in enumerate(lista):
        if x == valor:
            return x
    return None


l = [15, 25, 30, 35]
print(pesquisa(l, 25))
print(pesquisa(l, 41))


print(print.__doc__)

def diz_ola():
    ""Função que diz Olá Mundo!!!""
    return 'Olá Mundo!!!'


#print(diz_ola())

print(help(diz_ola))

print(diz_ola.__doc__)
""" 

def soma(a, b):
    print(a + b)

l = [2, 3]

soma(*l)