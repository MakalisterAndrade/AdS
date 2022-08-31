"""
Makalister Andrade da Silva - 21-02-2022
Funções


#Definindo uma função
def minha_funcao():
    print('Olá mundo!!!')
    print('Disciplina Estrutura de dados')
minha_funcao()

print(minha_funcao)
print(type(minha_funcao))

#Analise:
#A primeira linha define a função
#A segunda dá print a frase especificada(somente se a função for chamada)
#A terceira linha também da print(somente se a função for chamada)
#A quarta chama a função definida
#A quinta linha mostra o local em memória que a função está localizada
#A sexta linha diz o tipo de variável que é a função (que é função)


def minha_funcao_2(): #define a função
    soma = 0 # define a variavel soma como valor 0
    for i in range(0, 101):# diz que o indice dentro do intervalo 0 a 101
        soma += i #a soma terá o valor + o indice
    print(soma) #printa a variável soma

minha_funcao_2() # chama a função



def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('\n')

for i in range(5):
    print(i)
    cantar_parabens()
# A primeira linha define função
# A segunda à quinta linha dá print as frases
# A sexta linha pula uma linha
# A oitava linha diz que no intervalo de 0 a 5 irá ser dado print e chamada função
# A nona linha da print nos indices
# A décima linha chama a função


def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('\n')

cantar = cantar_parabens
cantar()

# A primeira linha define função
# A segunda à quinta linha dá print as frases
# A sexta linha pula uma linha
# A oitava a linha define a variável cantar iguala função já definida
# A nona linha chama a função por meio da variavel que foi igualada a ela



def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('\n')

cantar = cantar_parabens
cantar()

def quadrado_de_oito():
    return 8*8

ret = quadrado_de_oito()
print (ret)

# A primeira linha define função
# A segunda à quinta linha dá print as frases
# A sexta linha pula uma linha
# A oitava a linha define a variável cantar iguala função já definida
# A nona linha chama a função por meio da variavel que foi igualada a ela
# A décima primeira linha define a função
# a décima segunda linha retorna a multiplicação
# A décima quarta linha define a variável igual a função
# printa a variavel/função
"""