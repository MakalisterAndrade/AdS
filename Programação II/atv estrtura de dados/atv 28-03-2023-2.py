"""
Makalister Andrade da Silva - UTF8 - 28/03/2022

"""
#Desenvolvimento
#a
from tkinter.ttk import _TreeviewHeaderDict
from traceback import print_tb


cidades = [' ', 'Ariquemes',' ','Alto Paraíso',' ','Buritis','Cacaulândia',' ','Cacoal',' ','Castanheiras' ]
print(list(filter(lambda x: x.strip(), cidades)))

#b 
print()
def func(x):
    return x.split()


cidades = [' ', 'Ariquemes',' ','Alto Paraíso',' ','Buritis','Cacaulândia',' ','Cacoal',' ','Castanheiras' ]
print(list(filter(func, cidades)))

#c
twitter_usuarios = [
    {"nome":"Alexandre", "twets":["Gosto de doces", "Mas não curto brigadeiros"]},
    {"nome":"Jacob", "twets":[]},
    {"nome":"Everton", "twets": ["Cachorros são comanheiros"]},
    {"nome":"Alice", "twets":[]},
    {"nome":"Eduarda","twets": ["Cachorros são legais", "Mais gosto mesmo é de gatos"]},
    {"nome":}

]