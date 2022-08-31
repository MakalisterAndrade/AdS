"""
Makalister Andrade da SIlva 13-06-2022




# 1.1 - PILHAS — define a classe nó da lista encadeadas:

class No:
    def __init__(self, valor):
        self.valor = valor
        self.valor = None

    def mostra_no(self):
        print(self.valor)


# 1.2 - define a classe Lista_Encadeada e seus métodos

class Lista_Encadeada:

    def __init__(self):
        self.primeiro = None

    def lista_vazia(self, valor):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def exclui_inicio(self):
        if self.lista_vazia():
            print('A lista está vazia')
            return None

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp


# - Qual o local que no exemplo acima é considerado o topo da pilha? R:
# R. O ultimo objeto inserido

# 1.3 - defina a classe pilha lista encadeada e seus métodos para Pilhas

class Pilha_Lista_Encadeada:
    def __init__(self):
        self.lista = Lista_Encadeada()

    def empilha(self, valor):
        self.lista.insere_inicio(valor)

    def desempilha(self):
        return self.lista.exclui_inicio()

    def pilha_vazia(self):
        return self.lista.lista_vazia()

    def mostra_topo(self):
        if self.lista.primeiro == None:
            return f'pilha está vazia'
        return self.lista.primeiro.valor


#CIÊNCIA DE DADOS – Mineração de texto
# 1 - matplotlib.pyplot é um pacote integrado ao Python que possui uma coleção de
#funções para a criar figuras na área de plotagem. 

import matplotlib.pyplot as plt
# 2 - O NLP precisa do pacote nltk, por ser um pacote externo precisa de instalação:

#pip install nltk

# 2.1 - O pacote nltk não vem habilitado, para habilitá-lo faça o importe:

import nltk
#  2.2 – Para ler o arquivo e dividi-lo em delimitadores faça o importe da biblioteca
#PlaintextCorpusReader do pacote nltk:

from nltk.corpus import PLaintextCorpusReader


# 2.3 – Para retirar as palavras sem valor semântico do texto, faça o donwload


#(apenas uma vez) da biblioteca stopwords:

nltk.download()

# 2.3.1 – Se o download dos stopwords der erro execute o código abaixo:

'''
import ssl
try:
  _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
  pass
else:
  ssl._create_unverified_https_context = _create_unverified_https_context
  
nltk.download()
'''

# 2.3.1.1 – Para utilizar a biblioteca stopwords faça o importe: 

from nltk.cospus import stopwords

# 2.4 – Para criar um mapa de cores ao executar uma NLP, aplicamos o método matplotlib.colors
#da classe matplotlib.colors.ListedColormap, para habilitálo faça o importe:

from matplotlib.colors import ListedColormap

# 2.5 – Para criar a nuvem de palavras precisaremos do pacote externo
# wordcloud, por ser um pacote externo precisa de instalação

# pip install pip wordcloud

# 2.5.1 - O pacote wordcloud não vem habilitado, para habilitá-lo faça o
# importe do pacote junto com sua biblioteca:

from wordcloud import WordCloud

# 2.6 – Em ciência de dados muitas vezes precisamos fazer um import dinâmico
#para chamar um método utilizando o nome do método como uma string. A
#criação de uma nuvem de palavras é um desses momentos. Para essa
#ação precisaremos da biblioteca integrada string do Python,
#para habilitála faça o importe

import string

# 3 – Defina o corpus informando a pasta onde está o texto que armazenado. 
corpus = PLaintextCorpusReader('texto', 'vidavirtual.txt', encoding = 'utf-8')

'''- Corpus = é o nome da variável que irá receber o caminho onde está o texto;
- PlaintextCorpusReader(): método do ntk que vai ler o caminho onde está o texto;
- ‘Texto’: é o diretório onde está o texto a se lido;
- ‘vidavirtual.txt’: é o arquivo texto que será lido;
- encoding = “utf-8”: para textos formato brasileiro. 
'''

# 3.1 - Tipo de objeto que foi gerado: corpus = PlaintextCorpusReader(...)

print('>>> Tipo de texto instanciado <<<<')
print(type(corpus))
print()
print(input('>>> Enter - para continuar <<<'))

# Printa na tela o frase formatada
# Printa o tipo do texto corpus

# 3.2 - Corpus instanciado:

print(">>> Corpus do texto instanciado <<<")
print('- 2 cliques para ler o texto instanciado -')
print()
texto = corpus.raw()
print(texto)
print()
print(input('>>> Enter - para continuar <<<'))


# O método raw() coloca na string texto todo o conteúdo do artigo.

# 3.3 - Quantidade de caracteres com stopwords

print()
print(input(">>> Enter - quantidade de caracteres do texto com stopwords <<<"))
print(f'O texto tem: (len(texto)) caracteres incluindo as stopwords')
print()
print(input('>>> Enter - para continuar <<<'))

# 3.4 - Quantidade de palavras com stopwords

print
print(input('>>> Enter - quantidade de palavras do texto com stopwords <<<'))
palavras = corpus.words()
print(f'O texto tem: {len(palavras)} palavras incluindo as stopwords')
print()
print(input('>>> Enter - para continuar <<<'))

# 3.5 - Acessando palavra pelo índice

print
print(input('>>> Enter - Acessando palavra no texto com stopwords pelo índice = O <<<'))
print(f'A palavra que está no índice O do texto é: {palavras[0]}')
print()
print(input('>>> Enter - para continuar <<<'))

# 3.6 - Obtendo as stopwords em português

print(input('>>> Enter -Obtendo as stopwords em português <<<'))
stop_word = nltk.corpus.stopwords.words('portuguese')
print()
print(f'As stopwords em português são:')
print()
print(stop_word)
print()
print(input('>>> Enter - para continuar <<<'))
print()

# 3.7 - Obtendo mapa de cores

mapa_cores = ListedColormap(['orange', 'green', 'red', 'magenta'])

# 3.8 - Definindo a nuvem de palavras sem as stopwords

print(f'# 3.8 - Definindo a nuvem de palavras sem as stopwords')
nuvem = WordCloud(background_color = 'white'),
        colormap = mapa_cores,
        stopwords = stop_word,
        max_words = 500)
print(input('     - Enter - para continuar'))

# 3.9 - gerando a nuvem de palavras

print(f'# 3.9 - gerando a nuvem de palavras')
nuvem.generate(texto)
print(input(' - Enter - para continuar'))


# 3.10 - Plotando a nuvem de palavras

nuvem.generate(texto)
plt.imshow(nuvem, interpolation="None")
plt.axis('off')
plt.show()

# - Resultado
"""

# DESENVOLVENDO INTERFACES GRÁFICAS

#  desenvolvendo uma ‘interface’ gráfica padrão com Python e tkinter

# 1.1 — Implementando interface gráfica padrão com Python e tkinter

import tkinter

janela_principal = Tk()
janela_principal.mainloop()

# 2 – Configurando a Janela com Python / tkinter

from tkinter import *

janela = Tk()

# configurações da janela

janela.title('Curso de Analise e desenvolvimento de Software - IFRO')
janela.geometry('1360x670')  # É largura e a altura
janela.configure(background='#F8F8FF')  # cor de fundo
janela.resizable(True, True)  # ativa responsividade
janela.maxsize(width=1360, height=670)  # tamanho maximo a redimensionar
janela.minsize(width=1350, height=660)  # tamanho minimo a redimensionar

# 2.2.3 – FRAME – inserindo e posicionando um frame em uma janela

frame_1 = Frame(janela, borderwidth=1, relief='solid')
frame_1.place(x=10, y=10, width=1340, heigh=340)

# 2.2.3 — posicionando o frame 1 emx10€ey 10 pixels

frame_1.place(x=10, y=10, width=1340, heigh=340)

# 2.2.3.1 - inserindo e posicionando um Label dentro do frame_1

lb_1 = Label(frame_1, text='Agenda de Contatos:', fg='#FFFFOO0', font=("Arial", 18, "italic", "bold"))
lb_1.place(x=3, y=10, width=185, height=30)

# 2.2.3.1.1.1 - Label "Digite um nome:" dentro do frame_1

lb_2 = Label(frame_1, text='Digite um nome: ', font=("Arial", 16))
lb_2.place(x=20, y=40, width=120, height=30)

lb_3 = Label(frame_1, text='E-mail: ', font=("Arial", 16))
lb_3.place(x=20, y=40, width=120, height=30)

lb_4 = Label(frame_1, text='Telefone: ', font=("Arial", 16))
lb_4.place(x=20, y=40, width=120, height=30)

lb_5 = Label(frame_1, text='valor por Hora: ', font=("Arial", 16))
lb_5.place(x=20, y=40, width=120, height=30)

# 2.2.3.1.1.2 – função Entry() dentro do frame_1

nome = Entry(frame_1)
nome.place(x=140, y=40, width=300, height=30)

# 2.2.3.1.1.1 — Ação - cadastra dados capturados e grava

from tkinter import *
from tkinter import ttk


def cadastra():
    print('teste')
'''Defina um local para adicionar o Button(), em nosso exemplo será no final
do frame_1, adicione o button “Cadastrar”;
- A função que adiciona um botão é a Button()
- Associe o função Button() a uma variável;
- Coloque quem é o pai do botão dentro da função e depois virgula;
- Defina o texto que aparecerá no botão com o comando text = ‘aaa’;
- Após coloque uma virgula,
- Escreva command = nome_da função – esse comando chama a função
que será vinculada ao Button();
- Feche o parêntese da função Button();
- Posicione o botão na tela usando o gerenciador de layout place();'''

# 2.2.3.1.1.2 – Definindo um botão

btn_1 = Button(frame_1, text = 'Cadastrar', command = cadastra)
btn_1.place(x = 20, y = 290, width = 90, height = 30)

def cadastra():
        lb_2 = Label(frame_1, text = 'Nome: %s' % nome.get(), bg = '#F8F8FF', font=("Arial",16,"bold"))
        lb_2.place(x = 20, y = 180, width = 250, height = 30)

# A funçao get() retorna o valor do texto que foi digitado.

# 3 – lista dentro de listas;

listaNomes =[['0', 'Gertrudez', '69991234567'], ['1', 'Gerimunda', '69998912345'], ['2', 'Gnomica', '69998943214']]

# instanciamento e configurações

trvi = ttk.Treeview(janela, columns = ('id', 'no', 'fo'), show = 'headings')

# referencias para o cabeçalho


trvi.column('id', minwidth = 0, width = 50)

# defina o título do cabeçalho das colunas da Treeview;

trvi.headings('id', text = 'CODIGO')

# - configurando o titulo do cabeçalho das colunas da Treeview

trvi.heading('id', text = 'CODIGO')

# - configurando mostrar a Treeview na tela

trvi.place(x=10, y=370, width=1340, heigh=340)

# - inserindo dados das sub-listas na Treeview

for (i,n,f) in listaNomes:
    trvi.insert("", "end", values=(i, n, f))

janela.mainloop()









