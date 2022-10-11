"""
# Exercício: Desenvolva um script usando tkinter onde o operador irá digitar os
#dados cadastrais dos funcionários de uma empresa nos seguintes campos:
#Nome completo, a idade em meses, salário em real, e-mail e observações.
#Atenção: Para esse exercício não há necessidade de persistência dos dados
#em containers ou arquivos.
"""

import tkinter as tk
import turtle


def do_stuff():
    for color in ["red", "yellow", "green"]:
        my_lovely_turtle.color(color)
        my_lovely_turtle.right(120)


def press():
    do_stuff()
window = tk.Tk()

canvas = tk.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root)
    canvas.config(width=600, height=200)
    canvas.pack(side=tk.LEFT)
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("cyan")
    button = tk.Button(root, text="Confirma", command=press)
    button.pack()
    my_lovely_turtle = turtle.RawTurtle(screen, shape="turtle")
    root.mainloop()
