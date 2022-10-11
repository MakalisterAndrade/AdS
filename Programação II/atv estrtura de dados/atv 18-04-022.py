"""
Makalister Andrade da Silva - UTF8 - 02/05/2022
Atividades não presenciais(ordenando listas,tuplas,bibliotecas)


#atividade a

frutas = ['banana', 'maçã', 'abacaxi', 'pêra', 'melância', 'manga', 'goiaba', 'mamão', 'kiwi', 'abacate', 'maracujá', 'amora', 'uva', 'ameixa']
print()
print(frutas)
print()
frutas.sort()
print(frutas)
print()
frutas.sort(reverse=True)
print(frutas)
print()

#atividade b
sete = {12,2,3,45,84,1,87,10,5,8,96,105,15, 17, 32}
print(sete)
print(sorted(sete))
print()
sorted(sete)
print(sorted(sete, reverse=True))

"""

#atv f
"""

list_1 = [ str(input('Digite um nome: ')) for n in range(1,6)]
try:
    list_1 = [ str(input('Digite um nome: ')) for n in range(1,6)]
if list_1 == int or input:
    raise ValueError("That is not a positive number!")
except:

"""

#atv j
frutas = ['banana', 'maçã', 'abacaxi', 'pêra', 'melância', 'manga', 'goiaba', 'mamão', 'kiwi', 'abacate']
set(frutas)
print(sorted(frutas, reverse=True))
print(set(frutas))

#atv k
for letra in reversed('Campus Ariquemes'):
    print(letra, end=' ')

# cria um for que percorre a str e que reverte a ordem da string as separando em um espaço e printando na tela

#atv L
