"""Makalister Andrade da Silva - UTF8
Sábado Letivo 06-08-2022 a 07-08-2022"""

arquivo = open('candidatos.txt', 'w')
opt = ''
while opt != 0:
    print('''MENU
    [1] Ver resultados
    [2] Votar
    [0] Sair
    ''')
    def lerarq():
        arquivo = open('candidatos.txt', 'r')
        candidatos = []
        for linha in arquivo:
            linha = linha.strip()
            candidatos.append(linha)
        arquivo.close()

    opt = int(input("O que deseja fazer?: "))
    if opt == 1:
        lerarq()

    elif opt == 2:
        arquivo = open('candidatos.txt', 'w')
        eleitores = int(input("Digite o número total de eleitores: "))
        A = []
        B = []
        votantes = 0

        while (votantes < eleitores):
            voto = int(input("Digite 1 para votar no candidato a prefeito, 2 para o candidato a vereador: "))
            if (voto == 1):
                arquivo.write('prefeito\n')
            elif (voto == 2):
                arquivo.write('vereador\n')
            votantes = votantes + 1
        arquivo.close()
    elif opt == 0:
        break
    else:
        print("Opção inválida")




print("Programa cancelado")

