"""
Makalister Andrade da silva

# Exercício: Desenvolva um script usando tkinter onde o operador irá digitar os
#dados cadastrais dos funcionários de uma empresa nos seguintes campos:
#Nome completo, a idade em meses, salário em real, e-mail e observações.
#Atenção: Para esse exercício não há necessidade de persistência dos dados
#em containers ou arquivos.
"""
import tkinter as tk

class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.arquivoAberto = None
        self.criaWidgets()


    def criaWidgets(self):
        self.lbl1 = tk.Label(self.nossaTela, text="Nome Completo:", font=('Arial', 12))
        self.entNome = tk.Entry(self.nossaTela, font=('Arial', 12))

        self.lbl2 = tk.Label(self.nossaTela, text="idade em meses:", font=('Arial', 12))
        self.entmes = tk.Entry(self.nossaTela, font=('Arial', 12))

        self.lbl3 = tk.Label(self.nossaTela, text="Salário em real:", font=('Arial', 12))
        self.entsal = tk.Entry(self.nossaTela, font=('Arial', 12))

        self.lbl4 = tk.Label(self.nossaTela, text="E-mail:", font=('Arial', 12))
        self.entema = tk.Entry(self.nossaTela, font=('Arial', 12))

        self.lbl5 = tk.Label(self.nossaTela, text="Observações:", font=('Arial', 12))
        self.entobs = tk.Entry(self.nossaTela, font=('Arial', 12))


        self.cadastra = tk.Button(self.nossaTela, text="Cadastrar", )
        self.sair = tk.Button(self.nossaTela, text='Sair', command=self.nossaTela.quit)


        self.lbl1.grid(column=0)
        self.entNome.grid(row=0, column=1, padx=20)
        self.lbl2.grid(row=1, column=0)
        self.entmes.grid(row=1, column=1, padx=20)
        self.lbl3.grid(row=3, column=0)
        self.entsal.grid(row=3, column=1, padx=20)
        self.lbl4.grid(column=0)
        self.entema.grid(row=4, column=1, padx=20)
        self.lbl5.grid(column=0)
        self.entobs.grid(row=5, column=1, padx=20)
        self.cadastra.grid(row=6, column=0, columnspan=2, pady=20)
        self.sair.grid(row=7, column=0, columnspan=2, pady=20)
janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()