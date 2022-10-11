from lojaifro import *

it1 = Produto('1', 'smarttable', 'LG', '165', 1)

pedido = Pedido()

pedido.itens = it1

pedido.mostraPed()
#Pedido.total('1', 'smarttable', 'LG', 165, 1)