"""
Makalister Andrade da Silva - UTF8 - 14-02-2022

total =  0
def incrementa_total():
    total = total + 1
    return total

print(incrementa_total())

# Linha 4 declara a variavel global 'total' tem inteiro 0.
# linha 5 define a função 'incrementa_total' .
# Na linha 6 uma variável local 'total' é definida com valor (total + 1) dentro do escopo da função.
# Variável local 'total' referenciada antes da atribuição pois não é feita uma referencia a variavel global.
# na linha 7 retorna 'total' e termina a execução da função.
# Na linha 16 chamará a função 'incrementa_total' e dará print.
# O output daŕa erro devido a variavel local 'total' na função ter valor não referenciado
 
total = 0
def incrementa_total_2():
    global total
    total = total + 1
    return total

print(incrementa_total_2())
 
# Na linha  19 a variável global 'total' é criada com valor inteiro 0.
# Linha 20 a função define a função 'incrementa_total' .
#Linha 21 usa a expressão 'global' para referenciar a variavel global definida anteriormente 
# Linha 22 soma um ao 'total'.
# Linha 23 Retorna 'total' e termina a execução da função.
# Linha 25 chama a função'incrementa_total_2' e dá print.

def fora():
    contador =  0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()
print(fora())
print(fora())
print(fora())
print(fora())
print(fora())
 
# Linha 34 define a função 'fora' e a carrega na memória.
# Linha 35 cria uma variável local 'contador' que recebe o valor zero.
# Linha 36 define a função aninhada (nested) 'dentro'.
# Linha 37 referencia ao interpretador uma variável 'contador'
# que está definido na função 'fora' na linha 34.
#  Utiliza-se a expressão nonlocal em funções aninhadas.
# Linha 38 cria nova variavel local que é a Soma de um a 'contador' referenciada anteriormente.
# Linha 39 Retorna o valor de 'contador'.
# Linha 40 Retorna o valor que a função 'dentro' retornar.
# Linha 41 a 45 executam 'print' na função 'fora'. 
# 'contador' sempre é reiniciado ao chamar novamente a função.

def exponencial(n_1, potencia=4):
    """
    Função que retorna o quadruplo de um número;
    :parametro n_1: numero que será elevado a potencia;
    :parametro potencia: gera o exponencial por default é 4;
    :return: retorna o exponencial de n_1 por potencia
    """
    return n_1 ** potencia
print(exponencial.__doc__)
 
# Linha 59 define na memória a função 'exponencial' 
# Com dois parâmetros 'n_1' e 'potencia' com o valor quatro
# Linha 61 até 64 são uma docstring padrão que explica ao leitor do código
# a funcionalidade da função.
#Linha 66 retorna o cálculo da exponenciação  entre o primeiro parâmetro e o segundo
#Linha 67 dá 'print' na docstring da função


def verifica_inf(*args):
    if 'IFRO' in args and 'Campus Ariquemes' in args:
        return f'Bem vindo ao IFRO - Campus Ariquemes'
    else:
        return 'Eu não tenho certeza que você está no Campus Correto...'
print(verifica_inf())
print(verifica_inf(1, True, 'IFRO', 'Campus Ariquemes'))
print(verifica_inf(1, 'Campu', 256))


# Linha 77 define a  função 'verifica_inf' com vários parâmetros (*args)
# Linha 78 a 81 Verifica se 'IFRO' e 'Campus Ariquemes' são valores passados ​​como argumento.
# If yes, retorna uma mensagem formatada.
# Else, retorna outra mensagem formatada.
# Linha 82 chamrá e irá dar print na função 'verifica_inf'.
# Sem argumentos, retorna: Eu não tenho certeza...
# Linha 83 dá print na função com argumentos 'True', retorna: Bem vindo ao IFRO...
# Linha 83 dá print na função com argumentos 'False', retorna: Eu não tenho certeza...
 
def soma_todos_numeros(*args):
    return sum(args)
print(soma_todos_numeros())
print(soma_todos_numeros(1, 2, 3, 4))
numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_todos_numeros(*numeros))
 
# linha 96 define 'soma_todos_numeros' com vários parâmetros.
# linha 97 retorna a soma dos valores usando a função da bilioteca interna 'sum'.
# linha 98 chama e dá print na função 'soma_todos_numeros'.Sem argumentos return 0
# linha 99 chama e dá print na função com argumentos e retorna o valor
# linha 100 cria e salva uma lista na variável 'numeros'
# linha 101 dá print e chama a função e a lista 'numeros' é desempacotada (*) como parâmetro da funçãp.
 
def imprime_maior(mensagem, *numeros):
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
    print(mensagem, maior)
imprime_maior("Maior", 5, 4, 3, 2)
imprime_maior("Max", *[1, 7, 9, 11, 15])
 
# Linha 110 define a função 'imprime_maior' com parametros 'mensagem' e '*numeros'
# linha 111 a variável 'maior' é criada e recebe None como valor.
# Na linha 112 o laço for itera a variável 'e' sobre 'numeros'.
# Na linha 113 'if' verifica se 'maior' é 'None' ou menor que iterado 'e'
# linha 114 Caso sim, 'maior' passa a ser o iterado 'e'. 'For' executa até o final.
# Assim, o maior número é descoberto.
# linha 115 daprint ao argumento 'mensagem' e exibe o maior inteiro
# linha 116 e 117 chamam a função dando valores aos parametros
"""
def boas_vindas(**academicos):
    if 'ADS' in academicos and academicos['ADS'] == "Estrutura_dados":
        return f"Seja bem vindo ao mundo Pythônico acadêmico(a) de {academicos['ADS']}"
    elif 'ADS' in academicos:
        return f"{academicos['ADS']}"
    return 'Acredito que você não faça parte de nosso curso'
print(boas_vindas())
print(boas_vindas(ADS='Estrutura_dados'))
print(boas_vindas(ADS='Olá'))
 
# Linha 128 define a função'boas_vindas' com parametro '**academicos'.
# linha 128 a 132. condicional if-elif verifica os valores passados ​​como argumento
#  Caso qualquer valor seja passado na chave 'ADS', retorna esse valor.
#  Caso a chave 'ADS' tenha o valor 'Estrutura_dados'
# retorna 'Seja bem vindo ao mundo Pythônicp...'
# Na linha 133 caso não seja passada a chave 'ADS', retorna que 'Acredito que você não faça parte de nosso curso'.
# linha 134 chama e da print na função 'boas_vindas'
# linha 135 chama e da print na função 'boas_vindas'. Retorna: Seja bem vindo ao mundo Pythônico..
# linha 136 chama e da print na função 'boas_vindas'. Retorna: Olá
 
def mostra(a, b, *args, professor="Claudinei", **kwargs):
    return [a, b, args, professor, kwargs]
print(mostra(14, 21, 34, sobrenome='de Oliveira', cargo='Prof. EBTT área informática'))

# Linha 148 define a função 'mostra' que recebe 'a', 'b, '*args', 'professor='Claudinei'' e '**kwargs'
# Linha 149 retorna como lista com todos os valores recebidos como argumento.
# linha 150 dá print e chama a função 'mostra' com os valores dados aos argumentos.


def mostra_2(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"
nomes = {'nome': 'Gerimunda', 'sobrenome': 'da Silva'}
print(mostra_2(**nomes))
 
# linha 157 define a função 'mostra_2' que recebe '*kwargs'
# linha 158 retorna formatado os valores recebidos com as chaves 'nome' e 'sobrenome'
# linha 159 cria uma variavel 'nomes' com um dicionário de chaves 'nome' e 'sobrenome'.
# linha 160 da print na função 'mostra_2' que recebe a variavel(dict) 'nomes'
 
def multiplos_numeros(a, b, c):
    print(a + b + c)
lista = [11, 12, 13]
multiplos_numeros(*lista)
tupla = (1, 2, 3)
multiplos_numeros(*tupla)
conjunto = (3, 2, 1)
multiplos_numeros(*conjunto)
dicion = dict(a = 21, b = 42, c = 43)
multiplos_numeros(**dicion)
 
# Linha 167 define a função 'multiplos_numeros' com os parâmetros 'a', 'b' e 'c'.
# Linha 168 printa o resultado da soma entre os três/concatena se for string.
# Linha 169 cria uma lista com três inteiros. 
# Linha 170 Chama a função 'multiplos_numeros' desembalando os valores em lista.
# Então, printa 'multiplos_numeros'
# Linha 171 cria uma tupla com três valores.
# Linha 172 Chama 'multiplos_numeros' desempacotando os valores
# Então chama e printa 'multiplos_numeros'.
# Linha 173 cria outra tupla com três valores.
# Linha 174 chama 'multiplos_numeros' desempacotando os valores
# Então, printa a soma de'multiplos_numeros'
# Linha 175 cria um dicionário através da função dict com três valores.
# Linha 176 chama 'multiplos_numeros' desempacotando os itens do dicionário
 
def agencia(**carro):
    return carro
print(agencia(marca = 'Ford', modelo = 'K Sedan', cor = 'Azul', motor = '1.0'))
 
# Linha 192 define a função 'agencia', que recebe '*carros'.
# Linha 193 retorna os parâmetros/valores Recebidos.
# linha 194 printa o retorno da função 'agência' que recebe diversas variáveis.
# Na forma de dicionário:
# {'marca': 'Ford', 'modelo': 'K Sedan', 'cor': 'Azul', 'motor': '1.0'}
 
lista_lc_2 = [x * 2 for x in [3, 6, 9, 1]]
print(lista_lc_2)

# Linha 202 cria list compreh. que 'for' percorre uma lista
# usando o iterador 'x' e multipla o valor de 'x' por dois.
# Guarda a lista na variável 'lista_lc_2'
# Linha 203 printa lista_lc_2
 
lista_lc_3 = [(x, x * 2) for x in [1, 2, 3, 4]]
print(lista_lc_3)
 
# Linha 210 cria list compreh. que 'for' percorre uma lista usando o iterador 'x'.
# Dentro de uma tupla é salvo 'x' e multiplicado por dois.
# Que é guardado como lista na variável lista_lc_3.
# Linha 211 dá print lista_lc_2
 
nr = [1, 2, 3, 4, 5]
resultado = [numero * 15 for numero in nr]
print(resultado)
 
# Linha 218 cria uma lista 'nr' com inteiros
# Linha 219 cria uma list compreh. que 'for' percorre 'nr' usando o iterador 'numero'
# multiplica 'numero' por quinze. Salvo como lista na variável resultado.
# Linha 220 dá print em 'resultado'
 
lista_lc_4 = [letras.upper() for letras in 'abcdefgh']
print(lista_lc_4)
 
#Linha 227 cria uma list compreh. que 'for' percorre a string 'abcdefgh'
# com o iterador 'letras'. Cada letra da string é formatada em maiúsculo com método 'upper'.
# Salvo como lista na variavel variáveis_lc_4.
# Linha 228 dá print na lista 'lista_lc_4'

lista_lc_5 = [x for x in range(10) if x % 2 == 0]
print(lista_lc_5)
 
# Linha 235 cria uma List compreh. que 'for' percorre um intervalo itera com 'x'
# em que 'if' verifica se o 'x' é par. 
# Se for, é salvo dentro da lista 'lista_lc_5'.
# Linha 236 dá print na lista 'lista_lc_5'
 
list_lc_nome = [input('Digite um nome: ') for i in range(0, 3)]
print(list_lc_nome)
 
# Linha 243 cria uma list compreh. que 'for' itera em 'i'.
# e solicita ao usuário três vezes para digitar um nome.
# O que o usuário digitar será salvo na variavel 'list_lc_nome' como lista
# Dá print na lista 'list_lc_nome'
 
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)
    print(numeros_dobrados)
 
#  Cria a variável 'numeros' que recebe uma lista com cinco inteiros.
#  Cria a variável 'numeros_dobrados' que recebe uma lista vazia.
# 'for' itera 'numero' sobre a lista 'numeros'.
# A variável 'numero_dobrado' recebe 'numero' multiplicado por dois.
# Adiciona 'numero_dobrado' na lista 'numeros_dobrados'.
# printa a lista 'numeros_dobrados'.
  
numeros = [1, 2, 3, 4, 5]
print([numero * 2 for numero in numeros])
 
# Linha 265 cria uma lista com inteiros
# Linha 266 cria uma list compreh. que 'for' percorre a lista 'numeros' e salva 'numero' * 2.
# E dá print no resultado.
 
def maiuscula(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome
academicos = ['patricia', 'jacob', 'isaias', 'makalister', 'murillo', 'josias', 'Thauan']
print([maiuscula(academico) for academico in academicos])
 
 
# Define a função 'maiuscula' que recebe o parâmetro 'nome'
# Substitui a primeira letra do nome pela mesma letra em maiúsculo
# e salva em 'nome'.
# Retorna o valor da variável 'nome'.
# Define uma lista 'academicos' com diversos nomes.
# Cria uma List compreh. que 'for' percorre a lista  'academicos'
# passando cada um desses elementos como argumento para a função
#  'maiuscula'. Salvo numa lista. E printa.


print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
# Cria uma list compreh. que percorre uma lista com vários tipos e os tipa como 'bool'.
# Dá print se é True ou FAlse
 
print([str(nr) for nr in [1, 2, 3, 4, 5]])

# Cria uma list compreh. que transforma cada inteiro em string. E os printa
 
numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)
 
# Linha 297 Cria uma variável 'numeros' com uma lista com inteiros.
# Linha 298 cria uma list compreh. que armazena os números pares na variável 'pares'.
# Linha 299 cria uma list compreh. que  armazena os números ímpares na variável 'impares'.
# Linha 300 Printa 'pares'
# Linha 301 Printa 'impares'
 
 
numeros = [1, 2, 3, 4, 5]
resultado = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(resultado)
 
# linha 310 Cria uma variável 'numeros' com uma lista com inteiros.
# linha 311 cria um Dict compreh. que 'for' percorre a lista 'numeros' com
# o iterador 'num'. Cada 'num' é passado por uma condicional
# que determina se é par ou não. Caso par, o dicionário recebe 'num'
# como chave e 'par' como valor. Caso ímpar, o dicionário recebe o 'num'
# como chave e 'ímpar' como valor. O dicionário é salvo na variável 'resultado'
# printa 'resultado'
 
lista_lc_6 = [(y, x) for x, y in [(4, 3), (1, 2), (8, 9)]]
print(lista_lc_6)
 
# Cria uma dict compreh. que 'for' desempacota uma lista
# com várias tuplas nas variáveis ​​'x' e 'y'.
# Salva na ordem inversa 'y' e 'x' na variável 'lista_lc_6'.
# Dá print na lista 'lista_lc_6'
 
lista_lc_7 = [(x, y) for *x, y in [(4, 2, 3), (5, 1, 2), (7, 8, 9)]]
print(lista_lc_7)
 
# list compreh. que 'for' desempacota uma lista
# com várias tuplas nas variáveis ​​'x' e 'y'.
# temos '*x' e três valores em cada tupla, portanto os dois primeiros
# ficam em uma lista e o terceiro fica sozinho.
# Por fim, 'x' e 'y' estão inseridos em uma tupla e ainda dentro de 'lista_lc_7'.
# Dá print 'lista_lc_7' 
 
lista_lc_8 = [(x, y) for x, *y in [(4, 2, 3), (5, 1, 2), (7, 8, 9)]]
print(lista_lc_8)
 
# List compreh. 'for' desempacota uma lista com várias tuplas nas variáveis
#  'x' e 'y' com *y  três valores em cada tupla,
# portanto o primeiro fica sozinho e os dois últimos dentro de uma lista. 
# Por fim, 'x' e 'y' são inseridos em uma tupla e ainda dentro de 'lista_lc_8'.
# Printa 'lista_lc_8'
 
 
import math
lista_lc_9 = [math.sqrt(z) for z in range(3, 10)]
print(lista_lc_9)
 
# Linha 350 importa o pacote 'math'
# Linha 351 cria uma list comprehension com 'for' e iterador 'z' que percorre o range(3, 10)
# e processa a raiz quadrada através da função 'sqrt' de 'math'.
# Salva na 'lista_lc_9'.
# Dá print em 'lista_lc_9'.
 
import math
# % 1 == 00 ==> raiz quadrada exata inteira
lista_lc_10 = [x for x in range(3, 10) if math.sqrt(x) % 1 == 0]
print(lista_lc_10)
 
# Linha 360 importa o pacote 'math'.
# linha 361 comentario sobre como codar uma raiza exata inteira
# linha 362 cria uma list compreh. com 'for' e iterador 'x' percorre
# range(3, 10) e processa raiz quadrada através da função 'sqrt' de 'math'.
# Processa se uma raiz quadrada inteira for possível com a  condicional '% 1 == 0'.
# Salva na 'lista_lc_10'.
# linha 383 dá print em 'lista_lc_10'
 
numero = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave : valor ** 2 for chave, valor in numero.items()}
print(quadrado)
print(type(quadrado))
 
# linha 373 cria uma vriável 'numero' para armazenar um dicionário.
# linha 374 cria um Dict comprehension que percorre o dicionário 'numero'
#      e adiciona 'chave' como chave e 'valor ** 2' 
#      (exponenciação) como valor os guardando na variável 'quadrado'.
# linha 375 dá print no dicionário 'quadrado'
# linha 376 dá print no tipo da variável 'quadrado': dicionário (<class 'dict'>).
 
numeros = [1, 2, 3, 4, 5]
quadrados = {valor : valor ** 2 for valor in numeros}
print(quadrados)
 
# Linha 407 cria uma Variável e a popula com uma lista de inteiros.
# linha 408 dict compreh. que percorre a lista 'numeros'
# e adiciona 'valor'(inteiro da lista) como chave e 'valor ** 2'
# (exponenciação) como valor no dicionário e os salva na variável quadrado.
# linha 409 dá print em 'quadrado': {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
 
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
miscelania = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(miscelania)

# Linha 399 cria uma variavel 'chaves' que recebe uma string 'abcde'
# Linha 400 Cria a variavel 'valores' e a popula com a lista [1, 2, 3, 4, 5]
# Linha 401 cria a Dict compreh. que itera 'i' em um intervalo de zero até o tamanho
# da string 'chaves', e armazena como chave cada letra da string 'chaves' e como valor
# cada inteiro da lista 'valores' e é salvo na variável 'miscelânia'.
# linha 402 dá print no dict moscelania
 
 
numeros = [1, 2, 3, 4, 5]
resultado = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(resultado)
 
# Linha 412 cria uma variável 'numeros' com uma lista com inteiros(int).
# Na linha 413 cria uma dict compreh. em que 'for' percorre a lista 'numeros' com
# a ajuda do iterador 'num'. Cada 'num' é passado por uma condicional para ver sde é par ou impar
# O dicionário é salvo na variável 'resultado'.
# Dá print em 'resultado'.
 
nrs = {num for num in range(1, 7)}
print(nrs)
 
# Na linha 445 cria um list comprehension com 'for' e iterador 'num' no range(1, 7).E o guarda na variável 'nrs' como lista.
# Linha 446 dpa print a lista 'nrs'
 
nrs = {x: x ** 2 for x in range(1, 10)}
print(nrs)
 
# linha 428 define o Dict comprehension com 'for' e iterador 'x' no range(1, 10).
#   Guarda como chave 'x' e como valor a exponenciação 'x ** 2' Na variável 'nrs'.
# linha 429 dá print a variavel(dict) 'nrs'
 
letra = {letra for letra in 'Instituto Federal de Rondonia'}
print(letra)
 
# linha 435 define um Set comprehension que percorre com 'for' cada 'letra' (iterador) da string.
#  Cada 'letra' é salva na variável.
# linha 436 dá print ao conjunto 'letra' na tela: 
# Por se tratar de um conjunto não há repetições (inclusive espaços)e não está ordenado.
