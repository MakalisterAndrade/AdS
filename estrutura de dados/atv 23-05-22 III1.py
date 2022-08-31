"""
Makalister Andrade da Silva - UTF8 - 23-05-22


Programação orientada a objetos e listas simplesmente encadeadas

#PRINCIPAIS ELEMENTOS DA ORIENTAÇÃO A OBJETOS

#- Classe: = modelo do objeto do mundo real - computacionalmente
#- Atributo: = características do objeto;
#- Construtor: método especial utilizado para criar os objetos;
#- Método: = Comportamento do Objeto (funções);
#- Objeto: = chamado de instancia da classe.

#01 - Criando classes - atributos de instâncias - Lampada
class Lampada:
    def __init__(self,voltagem,cor,tipo,lumens,ligada): # __init__ método construtor
        self.voltagem = voltagem
        self.cor = cor
        self.tipo = tipo
        self.lumens = lumens
        self.ligada = False # constante

# 02 - Conta bancária tipo poupança

class ContaPoupanca:
    def __init__(self,titular, agencia, conta, senha, saldo):
        self.titular = titular
        self.agencia = agencia
        self.conta = conta
        self.senha = senha
        self.saldo = saldo
        
# 03 - Usuário de uma plataforma

class User:
    def __init__(self, nome, email, senha, ):
        self.nome = nome
        self.email = email
        self.senha = senha


# 04 - Produtos para uma loja de computadores
class ProdutosLoja:
    def __init__(self,tipo,codigobarr,codigoint,preco):
        self.tipo = tipo
        self.codigobarr = codigobarr
        self.codigoint = codigoint
        self.preco = preco


# 05 – Refatore o atributo de instância – da classe Lâmpada = #01, como privado;
class Lampada:
    def __init__(self,voltagem,cor,tipo,lumens,ligada): # def __init__ = método construtor
        self.__voltagem = voltagem
        self.__cor = cor
        self.__tipo = tipo
        self.__lumens = lumens
        self.__ligada = False


# 06 – Refatore o atributo de instância – da classe Conta bancária tipo poupança = #02,como privado;
class ContaPoupanca:
    def __init__(self,titular, agencia, conta, senha, saldo):
        self.__titular = titular
        self.__agencia = agencia
        self.__conta = conta
        self.__senha = senha
        self.__saldo = saldo


# 07 – Refatore o atributo de instância – da classe Usuário de uma plataforma = #03, como privado;
class User:
    def __init__(self,nome,email,senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha


# 08 – Refatore o atributo de instância – da classe Produtos para uma loja de computadores = #04, como privado.
class ProdutosLoja:
    def __init__(self,tipo,codigobarr,codigoint,preco):
        self.__tipo = tipo
        self.__codigobarr = codigobarr
        self.__codigoint = codigoint
        self.__preco = preco



# 09 - Criando Atributos de instância público e privado em uma classe
class Login:
    def __init__(self,nome,senha):
        self.nome = nome
        self.__senha = senha


# 10 – Instanciando e acessando Atributos de instância da classe Login

operador = Login('Makalister', '1234@1234')

print(operador.nome)

#print(operador.__senha)


# 11 - verificando as classes que estão relacionadas a um objeto instanciado.

print()
print(dir(operador))


# 12 – Imprimindo um o valor de um atributo de instancia privado.

print(operador._Login__senha) #Name Mangling, não recomendado
print()

# 13 - Criando e acessando Atributos de instância privado e público de uma classe

class Login2:
    def __init__(self,nome, senha):
        self.nome = nome
        self.__senha = senha
    
    def mostra_senha(self):
        print(self.__senha)

operador = Login2('Makalister', '1234@1234')

print(operador.nome)

operador.mostra_senha()

print()
operador_2 = Login2('Carla', '242432@242432')

print()
print(operador.nome)
operador.mostra_senha()

print()
print(operador_2.nome)
operador_2.mostra_senha()
print()

# 14 – Crie um método que apresente na tela todos os atributos de instância – da classe Lâmpada da #05, após apresente na tela o resultado.

#método construtor
class Lampada:
    def __init__(self,voltagem,cor,tipo,lumens,ligada): 
        self.__voltagem = voltagem
        self.__cor = cor
        self.__tipo = tipo
        self.__lumens = lumens
        self.__ligada = ligada

    def exibe_atributos(self):
        print(self.__voltagem)
        print(self.__cor)
        print(self.__tipo)
        print(self.__lumens)
        print(self.__ligada)

lampada = Lampada('Bivolt', 'Branca', 'Incandecente', '1200', True)
lampada.exibe_atributos()
print()


# 15 – Crie um método que apresente na tela todos os atributos de instância – da classe Conta bancária tipo poupança = #06, após apresente na tela o resultado. 
class ContaPoupanca:
    def __init__(self,titular, agencia, conta, senha, saldo):
        self.__titular = titular
        self.__agencia = agencia
        self.__conta = conta
        self.__senha = senha
        self.__saldo = saldo

    def mostrando_atributos(self):
        print(self.__titular)
        print(self.__agencia)
        print(self.__conta)
        print(self.__senha)
        print(self.__saldo)

poupanca = ContaPoupanca('Makalister', '1074-8', '74043-1','486235','R$ 2760,00')
poupanca.mostrando_atributos()
print()

# 16 – Crie um método que apresente na tela todos os atributos de instância – da classe Usuário de uma plataforma = #07, após apresente na tela o resultado. 
class User2:
    def __init__(self,nome,email,senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def exibir_atributos(self):
        print(self.__nome)
        print(self.__email)
        print(self.__senha)

user = User2('Andre', 'email@hotmail.com', 'senha@123')
user.exibir_atributos()
print()


# 17 – Crie um método que apresente na tela todos os atributos de instância – da classe Produtos para uma loja de computadores = #08, , após apresente na tela o resultado.
class ProdutosLoja:
    def __init__(self,tipo,codigobarr,codigoint,preco):
        self.__tipo = tipo
        self.__codigobarr = codigobarr
        self.__codigoint = codigoint
        self.__preco = preco

    def mostra_atributos(self):
        print(self.__tipo)
        print(self.__codigobarr)
        print(self.__codigoint)
        print(self.__preco)

item = ProdutosLoja('Notebook', '787464315487', '1596', 'R$ 2747,89')
item.mostra_atributos()
print()


#Atributos de classe: são valores dos atributos declarados diretamente na classe dentro do método construtor e que será compartilhado entro todas as instâncias das classes. 

#18 - Refatorando a classe Produto com atributo de CLASSE

class Produto:
    imposto = 1.08 #porcentagem do imposto sobre o produto (atributo de classe)

    def __init__(self,descricao,cor,marca,c_tecnica,valor):
        self.descricao = descricao
        self.cor = cor
        self.marca = marca
        self.c_tecnica = c_tecnica
        self.valor = (valor * Produto.imposto)

    def mostra_na_tela(self):
        print(self.descricao)
        print(self.cor)
        print(self.marca)
        print(self.c_tecnica)
        print(self.valor)

produto = Produto('Notebook gamer', 'Preto', 'Dell', 'Monitor 15,SSD M2 498Gb, RAM 32GB, Placa vídeo RTX3060', 13542.25)
produto.mostra_na_tela()

produto_2 = Produto('Magic Mouse 2 A1657', 'Branco', 'Apple', 'Espessura: 2,16cm, Comprimento: 5,71cm, Largura: 11,35cm, Peso: 0,099kg', 675.00)
produto_2.mostra_na_tela()


# 19 – Acessando um atributo de classe

print(Produto.imposto)


#Atributos Dinâmicos: são atributos criados em tempo de execução. Atenção: o
#atributo de dinâmico será exclusivo da instância que o criou

# 20 - Criando um atributo dinâmico - em tempo de execução – Não usual
produto.peso = '5kg' #na classe Produt não existe o atributo peso
produto_2.espessura = '216mm' #na classe Produto não existe o atributo espessura

print(f'Produto: {produto.descricao}, Cor: {produto.cor},Marca: {produto.marca}, Valor: {produto.valor}, Peso: {produto.peso}')
print()
print(f'Produto: {produto_2.descricao}, Cor: {produto_2.cor},Marca: {produto_2.marca}, Valor: {produto_2.valor}, Espessura: {produto_2.peso}')


# 21 - verificando a estrutura do objeto produto e produto_2

print(produto.__dict__)
print(produto_2.__dict__)


# 22 - verificando a estrutura da classe Produto
print(Produto.__dict__)


# 23 - deletando atributos dinâmicos ou de classe

del produto.peso
del produto.c_tecnica

del produto_2.espessura
del produto_2.c_tecnica

print(produto.__dict__)
print(produto_2.__dict__)


#LISTAS SIMPLESMENTE ENCADEADAS

# 1.1 – Importando a biblioteca numpy
from csv import list_dialects
#import numpy as np

# 1.1.2 – Definindo a Classe Nó
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None #sinal de nulo - fim da lista

# 1.1.2.1 – função mostra_no()
    def mostra_no(self):
        print(self.valor) #Apresenta o valor de cada nó


# script que recebe um nó do tipo número inteiro:
#no_1 = No(35)
#no_1.mostra_no()

# 2 – A partir da classe No pronta, desenvolva um script para receber 5 nós do tipo número inteiro e após apresentar na tela:
lista = No()

no_1 = No(12)
no_2 = No(14)
no_3 = No(16)
no_4 = No(18)
no_5 = No(20)

print(no_1.mostra_no())
print(no_2.mostra_no())
print(no_3.mostra_no())
print(no_4.mostra_no())
print(no_5.mostra_no())


# 2.1 – Criando classe para armazenar a estrutura de vários nós
class Lista_Encadeada:
    def __init__(self):
        self.primeiro = None

# 2.1 – Criando classe para armazenar a estrutura de vários nós
    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

# 2.1.2 – Implementando a função mostrar_na_tela() - apresentar o valor de vários nós na tela
    def mostrar_na_tela(self):
        if self.primeiro == None:
            print('A lista está vazia!!')
            return None
        atualiza = self.primeiro
        while atualiza != None:
            atualiza.mostra_no()
            atualiza = atualiza.proximo


# 2.1.3 – Inserindo o objeto 53
# 2.1.4 – Inserindo o objeto 90
# 2.1.5 – Inserindo o objeto 47
# 2.1.6 – Inserindo o objeto 15

# 3 – inserindo dados na lista simplesmente encadeada no Python
lista_s_e = Lista_Encadeada()

lista_s_e.insere_inicio(35)
print(f'O endereço da memória do elemento inserido na lista é: ',{lista_s_e.primeiro})
lista_s_e.mostrar_na_tela()

print()
lista_s_e.insere_inicio(53)
print(f'O endereço da memória do elemento inserido na lista é: ',{lista_s_e.primeiro})
lista_s_e.mostrar_na_tela()

print()
lista_s_e.insere_inicio(90)
print(f'O endereço da memória do elemento inserido na lista é: ',{lista_s_e.primeiro})
lista_s_e.mostrar_na_tela()

print()
lista_s_e.insere_inicio(47)
print(f'O endereço da memória do elemento inserido na lista é: ',{lista_s_e.primeiro})
lista_s_e.mostrar_na_tela()

print()
lista_s_e.insere_inicio(15)
print(f'O endereço da memória do elemento inserido na lista é: ',{lista_s_e.primeiro})
lista_s_e.mostrar_na_tela()

# 4 – Método exclui objeto no início da lista simplesmente encadeada. O objetivo é excluir o objeto da lista 
# simplesmente encadeada e retornar o valor para uma variável temporária.
# 4.1 – Criando o método exclui objeto no início da lista 
def excluir_inicio(self):
    if self.primeiro == None:
        print('A lista está vazia')
        return None
    temp = self.primeiro
    self.primeiro = self.primeiro.proximo
    return temp

# 4.2 – Implementando o método exclui objeto no início da lista
print()
print('Lista Original: ')
lista_s_e.mostrar_na_tela()

print()
print('Lista com o primeiro elemento excluído:')
lista_s_e.excluir_inicio()
lista_s_e.mostrar_na_tela()

print()
print('Lista com o primeiro elemento excluído:')
lista_s_e.excluir_inicio()
lista_s_e.mostrar_na_tela()

print()
print('Lista com o primeiro elemento excluído:')
lista_s_e.excluir_inicio()
lista_s_e.mostrar_na_tela()

print()
print('Lista com o primeiro elemento excluído:')
lista_s_e.excluir_inicio()
lista_s_e.mostrar_na_tela()

print()
print('Lista com o primeiro elemento excluído:')
lista_s_e.excluir_inicio()
print()
lista_s_e.mostrar_na_tela()


# 5 – Método pesquisar objeto. O objetivo é passar um valor e o script irá percorrer cada um dos objetos 
# contidos na lista e verificar se o objeto (valor foi encontrado). Se o objeto foi encontrado o script irá 
# retornar o valor do objeto, senão irá retornar None, indicando que o script não conseguiu encontrar.

# 5.1 – Implementando o método pesquisa objeto numa lista simplesmente encadeada.
def pesquisaObjeto(self):
    if self.primeiro == None:
        print('A lista está vazia')
        return None

        atualiza = self.primeiro
        while atualiza.valor != valor:
            if atualiza.proximo == None:
                return None
            else:
                atualiza = atualiza.proximo
        return atualiza


print()
print('Lista Original: ')
lista_s_e.mostrar_na_tela()

print()
pesquisa = lista_s_e.pesquisaObjeto(13)

print()
if pesquisa != None:
    print('Objeto encontrado: ',pesquisa.valor)
else:
    print('Objeto não encontrado')


#  5.2 – Faça a análise descritiva dos códigos acima, linha a linha apresentando  o resultado.

# Linha 430 a 433 cria o método de pesquisa com if dizendo que se o primeiro atributo estiver 
# Vazio (== None), PRinta frase na tela e retorna None em Background
# Linha 435 a 441  Cria a variavel atualiza que recebe o valor do primeiro objeto da lista
# Cria condição verificadora para saber se o objeto(.valor) é diferente do passado ao operador
# Se for verdadeiro entra na linha 437 e retorna None
# Se falso atualiza recebe o próximo objeto e retorna atualiza
# Linha 444 printa na tela a lista original após pular uma linha, e chama a função
# Linha 448 Pula linha, printa na tela e passa valor(13) para a variavel pesquisar
# Linha 452 a cria condição de que se pesquisa for diferente de None
# se verdadeiro
# Linha 453 printa na tela frase e objeto encontrado
#se falso
# Linha 455 Printa na tela objeto não encontrado


# 6 – Implementando o método excluiObjetoNaPosicao em uma lista simplesmente encadeada
def excluiObjetoNaPosicao(self, valor):
    if self.primeiro == None:
        print('A lista está vazia')
        return None
    elif valor not in lista_s_e:
        print('Não estána lista')
        return None

    atualiza = self.primeiro
    anterior = self.primeiro
    while atualiza.valor != valor:
        if atualiza.proximo == None:
            return None
        else:
            anterior = atualiza
            atual = atual.proximo

    if atualiza == self.primeiro:
        self.primeiro = self.primeiro.proximo
    else:
        anterior.proximo = atual.proximo
    return atualiza




print()
print(f'Excluindo objeto numa determinada posição: ')
lista_s_e.excluiObjetoNaPosicao(99)
lista_s_e.mostrar_na_tela()
"""