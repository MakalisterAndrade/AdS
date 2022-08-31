
from tkinter import *
from tkinter import messagebox


class GUI:
    def __init__(self):
        # janela principal
        self.janela_p = Tk()

        # Criando
        self.names = Frame(self.janela_p)
        self.idade = Frame(self.janela_p)

        self.frame_baixo = Frame(self.janela_p)

        # opções
        self.label = Label(self.names, text='Nome Completo:')
        self.label = Label(self.idade, text='idade em meses:')

        # Criando o widget de entrada
        self.entrada = Entry(self.names, width=30)
        self.entrada = Entry(self.idade, width=30)

        # Empacotando label e entrada no frame de cima
        self.label.pack(side='left')
        self.entrada.pack(side='left')

        # Criando os botões, no frame de baixo
        self.botao = Button(self.frame_baixo, text='Confirma', )
        self.botao_sair = Button(self.frame_baixo, text='Sair', command=self.janela_p.quit)

        # Empacotando os botões no frame de baixo
        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')

        # Empacotando os botões janela principal
        self.botao.pack()
        self.botao_sair.pack()

        # Empacotando os frames na janela principal
        self.names.pack()
        self.idade.pack()
        self.frame_baixo.pack()

        # Rodando
        mainloop()




gui = GUI()