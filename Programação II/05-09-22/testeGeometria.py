from Geometria import *

#q = Quadrado()
#r = Retangulo()
#c = Circulo()

quadrad = []
retang = []
circ = []

forms = int(input("Quantas formas geom. desejas criar?: "))
for i in range(0, forms):
    opt = 0
    opt = int(input('Deseja criar: \n'
                    '[1] Quadrado\n'
                    '[2] Retangulo\n'
                    '[3] Circulo\n'))
    if opt == 1:
        lado = Quadrado.lado
        lado = float(input("\n Informe o tamanhado dos lados do quadrado: "))
        quadrad.append(lado)
    if opt == 2:
        ladoa = Retangulo.lado2
        ladoa = float(input("\n Informe o tamanhado do lado 'A' do Retângulo: "))
        ladob = Retangulo.lado2
        ladob = float(input("\n Informe o tamanhado do lado 'B' do Retângulo: "))
        ladoc = Retangulo.lado3
        ladoc = float(input("\n Informe o tamanhado do lado 'C' do Retângulo: "))
        ladod = Retangulo.lado4
        ladod = float(input("\n Informe o tamanhado do lado 'D' do Retângulo: "))
        retang.append(ladoa, ladob, ladoc, ladod)
    if opt == 3:
        raio = Circulo.raio
        raio = float(input("\n Informe o tamanhanho do raio do Circulo: "))
        circ.append(raio)

print(f"Tamanhos dos lados dos Quadrados armazenados: {quadrad}")
print()
print(f"Tamanhos dos lados dos Retângulos armazenados: {retang}")
print()
print(f"Tamanhos dos raios dos Circulos armazenados: {circ}")

print(f'Cálculo de áreas: {Circulo.calcArea(5)}')



