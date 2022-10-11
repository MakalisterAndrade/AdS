"""
Makalister Andrade da Silva - UTF8 - pt-br - 16-02-2022
Manipulando MAPAS - iterando sobre dicionários

#atividade 1
receita_bruta = {'Janeiro':1500, 'Fevereiro':2650, 'Março':1450,'Abril':18000, 'Maio':2000, 'Junho':3150}

print(receita_bruta.items())

for chave, valor in receita_bruta.items():
    print(f'chave = {chave} e valor = {valor}')

# Análise:
# Na primeira linha de código (linha 6) são declarados as chaves e os valores
# Na segunda linha do código (linha 8)  é printado todos os itens do dicionário
# Na terceira linha do código (linha 10) é dito que para cada chave  e valor no dicionário
#  será printado item a item na tela
# O objetivo do script é printar os items de um dicionário(já populado) pyhton linha a linha
#  com formatação agrádavel ao usuário

#atividade 2
lista = [1, 2, 3, 4, 5, 6]
def multiplica(x):
    return x * 2

lista_1 = map(multiplica, lista)
print(lista_1)
print('\n')

print(list(lista_1))

print('\n')
print(list(map(multiplica, lista)))

# Análise
# Cria uma lista e define(popula) variáveis
# Define um parâmetro(x) para a função multiplica retornando o valor x*2
# Define a variável lista_1 como um mapa de objeto em memória
# map() então aplica a função multiplica a cada item da lista
# list() então cria uma lista com o mapa em memória
# print(list(map(multiplica, lista))) organiza e printa os passos anteriores

# atividade 3
tupla_1 = ('Seres Humanos', 'Família dos Cachorros', 'Família dos Gatos')
tupla_1
tupla_1[0]
tupla_1.index('Família dos Gatos')

for elemento in tupla_1:
    print(elemento)
# Análise
# A primeira linha do código declara os objetos da tupla
# As linhas 2 e 3(8 e 9) são basicamente lixo em memória já que não interferem no script
# A linha 10 retorna a primeira ocorrência do objeto específicado e também é lixo em memoŕia sem um print
# Linhas 12 e 13 iteram que para cada elemento na variável tupla 1 seja printado linha a linha os elementos


# atividade 4

lista_1 = ['Seres Humanos', 'Família dos Cachorros', 'Família dos Gatos']
lista_2 = ['rã-de-unhas-africanas', 'Panda Gigante']

lista_3 = lista_1 + lista_2

print(lista_3)
print(type(lista_3))
print(id(lista_3))

# Análise
# As duas primeiras linhas do script criam e populam uma lista com strings
# A terceira linha concatena duas lista para criar um nova
# A quarta linha printa a nova lista criada por concatenação
# A quinta e sexta linhas printam a classe do objeto e a posição em memória ocupada respectivamente

# atividade 5

dados = {'Dengue':32, 'Chicungunha':22, 'Covid19':1100}
print(dados)
print(dados['Covid19'])
del(dados)['Dengue']
print(dados)

print(dados.items())
print(dados.keys())
print(dados.values())

# Análise
# Na primeira linha é criado e populado um dicionário com chaves e valores
# Na segunda linha é exibido ao usário os items do dicionário
# Na terceira é printado o valor apenas da chave 'Covid19'
# A quarta linha dele a chave e valor de 'Dengue' do dicionário
# Na quinta linha é novamente printado dicionário, agora sem o item 'Covid19'
# As últimas 3 linhas printam respectivamente os items, chaves e valores do diocionário



# atividade 6
cj_1 = {1,2,3,4,5}
cj_2 = {3,4,5,6,7}
cj_3 = cj_1.intersection(cj_2)
print(cj_3)
print(cj_1.difference(cj_2))
print(cj_2.difference(cj_1))
print(cj_2.symmetric_difference(cj_1))

# Análise
# As duas primeiras linhas criam e populam um conjunto cada com valores inteiros
# A terceira e quarta linha,respectivamente, cria e printa um conjunto com os valores que se repetem(interseccionam) nas tuplas anteriores
# A quinta linha printa os valores que estão no conjunto cj_1 mas não no cj_2
# A sexta linha printa os valores que estão no conjunto cj_2 mas não no cj_1
# A sétima linha printa as difereças presetes(valores que não se repetem) entre os ois conjuntos
"""
