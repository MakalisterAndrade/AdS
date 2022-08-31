"""
Makalister Andrade da Silva - UTF8 - 23-05-22



"""

# 1.1 – Importando a biblioteca numpy
import numpy as np 

# 1.1.2 – Definindo a Classe No 
class No: 
    def __init__ (self, valor): 
        self.valor = valor 
        self.proximo = None 

# 1.1.2.1 – função mostra_no()
    def mostra_no(self): 
        print(self.valor)

# script que recebe um nó do tipo número inteiro:
# no_1 = No(35) 
# no_1.mostra_no() 

# 2 – A partir da classe No pronta, desenvolva um script para receber 5 nós 
# do tipo número inteiro e após apresentar na tela

# 2.1 – Criando classe para armazenar a estrutura de vários nós
class Lista_Encadeada: 

    def __init__(self):
        self.primeiro = None

# 2.1.1 – Método insere objeto no início da lista simplesmente encadeada

    def insere_inicio(self, valor): 
        novo = No(valor) 
        novo.proximo = self.primeiro 
        self.primeiro = novo 

# 2.1.2 – Desenvolver script para apresentar o valor de vários nós
#  na tela.
    def mostrar_na_tela(self): 
        if self.primeiro == None: 
            print('A lista está vazia') 
            return None 

        atualiza = self.primeiro 
        while atualiza != None:
            atualiza.mostra_no()
            atualiza = atualiza.proximo

# 3 – inserindo dados na lista simplesmente encadeada no Python


        lista_s_e = Lista_Encadeada() 

        lista_s_e.insere_inicio(35) 
        print(f'O endereço de memória do elemento inserido na lista é: {lista_s_e.primeiro}')
        lista_s_e.mostrar_na_tela() 

        print() 
        lista_s_e.insere_inicio(53)
        print(f'O endereço de memória do elemento inserido na lista é: {lista_s_e.primeiro}')
        lista_s_e.mostrar_na_tela() 

        print() 
        lista_s_e.insere_inicio(90)
        print(f'O endereço de memória do elemento inserido na lista é: {lista_s_e.primeiro}')
        lista_s_e.mostrar_na_tela()

        print() 
        lista_s_e.insere_inicio(47)
        print(f'O endereço de memória do elemento inserido na lista é: {lista_s_e.primeiro}')
        lista_s_e.mostrar_na_tela()

        print() 
        lista_s_e.insere_inicio(15)
        print(f'O endereço de memória do elemento inserido na lista é: {lista_s_e.primeiro}')
        lista_s_e.mostrar_na_tela()


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
        print('Lista original: ')
        lista_s_e.mostrar_na_tela()

        print()
        print(f'Lista com o primeiro elemento excluido: ')
        lista_s_e.excluir_inicio()
        lista_s_e.mostrar_na_tela()

        print()
        print(f'Lista com o primeiro elemento excluido: ')
        lista_s_e.excluir_inicio()
        lista_s_e.mostrar_na_tela()

        print()
        print(f'Lista com o primeiro elemento excluido: ')
        lista_s_e.excluir_inicio()
        lista_s_e.mostrar_na_tela()

        print()
        print(f'Lista com o primeiro elemento excluido: ')
        lista_s_e.excluir_inicio()
        lista_s_e.mostrar_na_tela()

        print()
        print(f'Lista com o primeiro elemento excluido: ')
        lista_s_e.excluir_inicio()
        lista_s_e.mostrar_na_tela()

        print()
        print(f'Lista com o primeiro elemento excluido: ')
        lista_s_e.excluir_inicio()
        print()
        lista_s_e.mostrar_na_tela()

#  5.1 – Implementando o método pesquisa objeto numa lista simplesmente encadeada

        def pesquisaObjeto(self, valor):
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
                print('Objeto encontrado: ', pesquisa.valor)
            else:
                print('Objeto não encontrado:')

#  5.2 – Faça a análise descritiva dos códigos acima, linha a linha apresentando  o resultado.

# Linha 132 a 135 cria o método de pesquisa com if dizendo que se o primeiro atributo estiver 
# Vazio (== None), PRinta frase na tela e retorna None em Background
# Linha 137 a 143  Cria a variavel atualiza que recebe o valor do primeiro objeto da lista
# Cria condição verificadora para saber se o objeto(.valor) é diferente do passado ao operador
# Se for verdadeiro entra na linha 140 e retorna None
# Se falso atualiza recebe o próximo objeto e retorna atualzia
# Linha 145 a 150 Pula linhas, printa na tela e passa valor(13) para pesquisar
# Linha 153 cria condição de que se pesquisa for diferente de None
# se verdadeiro
# Linha 154 printa na tela frase e objeto encontrado
#se falso
# Printa na tela objeto não encontrado


# 6.1 – Implementando o método excluiObjetoNaPosicao em uma lista simplesmente encadeada
            def excluiObjetoNaPosicao(self, valor): 
                if self.primeiro == None: 
                    print('A lista está vazia') 
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

    