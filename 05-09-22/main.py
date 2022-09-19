from model import Retangulo, Quadrado, Circulo

if __name__ == '__main__':
    quant = 0
    while True:
        try:
            quant = int(input('Quantas formas deseja criar?: '))
            break
        except ValueError:
            print("Quantidade inválida!!!")

    formas_geo = []
    i = 1
    while i <= quant:
        try:
            tipo = int(input('1 - Quadrado\n'
                             '2 - Retângulo\n'
                             '3 - Círculo\n'
                             'Tipo: '))
            if tipo == 1:
                lado = float(input('Informe o lado: '))
                quadrado = Quadrado(lado)
                formas_geo.append(quadrado)
            elif tipo == 2:
                base = float(input('Informe a base: '))
                altura = float(input('Informe a altura: '))
                formas_geo.append(Retangulo(base, altura))
            elif tipo == 3:
                raio = float(input('Informe o raio: '))
                formas_geo.append(Circulo(raio))
            else:
                print("Tipo inválido")
                continue
            i += 1
        except ValueError:
            print("Tipo inválido")
            continue

    print("\nImprimindo dados das formas geométricas:\n")
    for f in formas_geo:
        if isinstance(f, Circulo):
            print("===Círculo===")
            print(f'Raio: {f.raio:,.2f}')
        elif isinstance(f, Quadrado):
            print("===Quadrado===")
            print(f'Lado: {f.lado:,.2f}')
        elif isinstance(f, Retangulo):
            print("===Retângulo===")
            print(f'Base: {f.base:,.2f}\n'
                  f'Altura: {f.altura:,.2f}')
        print(f'Perímetro: {f.calcula_perimetro():,.2f}')
        print(f'Área: {f.calcula_area():,.2f}\n')