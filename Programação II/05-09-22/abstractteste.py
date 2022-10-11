from abstract import *

onibus1 = Onibus('NFT1234','2016',14)
print(onibus1.exibirDados())

onibus1.placa = 'ABC1234'
onibus1.ano = 2012
onibus1.assentos = 22

print(onibus1.exibirDados())

print()
caminhao1 = Caminhao('HJD1983','2022',4)
print(caminhao1.exibirDados())

caminhao1.placa = 'NJN4D15'
caminhao1.ano = 2010
caminhao1.eixos = 2

print(caminhao1.exibirDados())