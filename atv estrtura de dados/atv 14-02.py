"""
Makalister Andrade da Silva - UTF8-14-02-2022

#Tentando acessar uma chave de dicionário que não existe
#Dado o dicionário


disciplina_curso = {'disciplina':'Estrtura de dados'}

print(disciplina_curso)

print(disciplina_curso['disciplina'])

print(disciplina_curso['materia'])


from collections import defaultdict

disciplina_curso = defaultdict(lambda:'None')#não recebe valor e retorna None

print(disciplina_curso)

disciplina_curso['disciplina'] = 'Estrutura de dados'

print(disciplina_curso)

print(disciplina_curso['disciplina']) #chave existe

print(disciplina_curso['materia']) #chave não existe - mostra None na tela

print(disciplina_curso)

#Dado um dicio comum

nome_1 = {'Gustavo':28, 'André':33, 'João':15, 'Alice':9, 'Laís':5 }
print(nomes)
for chave, valor in nomes.items():
    print(f'chave{chave} : valor = {valor})
    

# Dados os dicionários comuns: - Igualdade
#Nos dicionários comuns o Python verifica se os elementos (chave: valor)
#existem no dicionário independente da ordem dos elementos. 

nome_1 = {'Gustavo':28, 'André':33, 'João':15, 'Alice':9, 'Laís':5 }
nome_2 = {'André':33, 'João':15, 'Gustavo':28, 'Laís':5, 'Alice':9,}

print(nome_1 ==nome_2)

#Nas operações de igualdade entre dicionários, o OrderedDict verifica se a
#ordem dos elementos são as mesmas



from collections import OrderedDict

#Dado um dicinário OrderedDict

nome_1 = OrderedDict({'Gustavo':28, 'André':33, 'João':15, 'Alice':9, 'Laís':5})
nome_2 = OrderedDict({'André':33, 'João':15, 'Gustavo':28, 'Laís':5, 'Alice':9,})

print(nome_1 == nome_2)


#move_to_end(): reposiciona um elemento
#para um endpoint. Por padrão o elemento é movido para o final do dicionário.

from collections import OrderedDict
nome_4 = OrderedDict({'Gustavo':28, 'André':33, 'João':15, 'Alice':9, 'Laís':5})
print(nome_4)
print(type(nome_4))
print('\n')

nome_4.move_to_end('André')
print(nome_4)
print(type(nome_4))
print('\n')


#move_to_end( chave, last = False) o elemento é movido
#o início do dicionário.

from collections import OrderedDict
nome_5 = OrderedDict({'Gustavo':28, 'André':33, 'João':15, 'Alice':9, 'Laís':5})
print(nome_5)
print(type(nome_5))
print('\n')

nome_5.move_to_end('Laís', last = False)
print(nome_5)
print(type(nome_5))
print('\n')

#Revisando tuplas
#Módulo Collections - Named Tuple: são tuplas que devemos especificar um
#nome e um parâmetro.


#namedtuple
# Forma_1 de declarar

from collections import namedtuple
animal = namedtuple('animal', 'tipo nome raca idade')
print(animal)

# Forma_2 de criar
from collections import namedtuple
animal = namedtuple('animal','tipo, nome, raca, idade')

# Forma_3 de criar
from collections import namedtuple
animal = namedtuple('animal', ['tipo','nome', 'raca', 'idade'])



#Populando a tupla nomeada
cachorros = animal(tipo = 'cachorro', nome = 'Hatch', raca='vira latas', idade = 2)
print(cachorros)
print(type(cachorros))

#Acessando dados
print(f'Tipo:{cachorros[0]}')
print(f'Nome: {cachorros[1]}')
print(f'Raça: {cachorros[2]}')
print(f'idade: {cachorros[3]}')

print('ou')


#Acessando dados
print(f'Tipo:{cachorros.tipo}')
print(f'Nome: {cachorros.nome}')
print(f'Raça: {cachorros.raca}')
print(f'idade: {cachorros.idade}')


#Módulo Collections - Deque: 
#Módulo de alta performance;
#Os elementos podem ser inseridos no início ou final do container;
#Os elementos podem ser apagados no início ou final do container.

from collections import deque
#criando
deq_1 = deque('Ariquemes')
print(deq_1)
print(type(deq_1))



from collections import deque
#adicionando elementos
# dado o deque
deq_2 = deque()

deq_2.append('Ariquemes')
print(deq_2)

deq_2.append('Curso de ADS')
print(deq_2)

deq_2.append('Campus')
print(deq_2)

deq_2.append('Ifro')
print(deq_2)
print(type(deq_2))


"""
Removendo elementos

from collections import deque
#Dado o deque

deq_3 = deque()
deq_3.append('IFRO')
deq_3.append('Campus')
deq_3.append('Ariquemes')
deq_3.append('-Curso de ADS')

print(deq_3)
print(type(deq_3))

print('\n')

print(deq_3.pop())# remove e retorna o elemento
print(deq_3)

print(deq_3.popleft())
print(deq_3)







