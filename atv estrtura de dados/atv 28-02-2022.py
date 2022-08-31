"""
Makalister Andrade da Silva - UTF8 - pt-br
Funções - DRY - Don't repeat Yourself
"""
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num %2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

print()

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))