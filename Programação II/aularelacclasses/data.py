"""
Makalister Andrade da Silva UTF8 15/08/2022
"""

'''
Crie uma classe chamada Data com os seguintes atributos: dia(int), mes(int), ano(int).  
Encapsule estes atributos (utilize todas as técnicas aprendidas).
Nos métodos “setter” faça validações para não permitir dias , meses e anos inválidos. 
A classe deve possuir ainda um método para retornar a data no formato “20/08/2021”.
'''

class Data():
    __slots__ = {'_dia',
                 '_mes',
                 '_ano'}

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self, dia):
        self._dia = dia

    @property
    def mes(self):
        return self._mes

    @mes.setter
    def mes(self, mes):
        self._mes = mes

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano
'''
def data_valida(data):
    try:
        # faz o split e transforma em números
        dia, mes, ano = map(int, data.split('/'))

        # mes ou ano inválido, retorna False
        if mes < 1 or mes > 12 or ano <= 0:
            return False

        # verifica qual o último dia do mês
        if mes in (1, 3, 5, 7, 8, 10, 12):
            ultimo_dia = 31
        elif mes == 2:
            if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
                ultimo_dia = 29
            else:
                ultimo_dia = 28
        else:
            ultimo_dia = 30

        # verifica se o dia é válido
        if dia < 1 or dia > ultimo_dia:
            return False

        return True
    except ValueError:
        return False

data_valida(2,3,12)
'''
valida = False

# Meses com 31 dias
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or \
mes == 8 or mes == 10 or mes == 12):
    if (dia <= 31):
        valida = True
# Meses com 30 dias
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if (dia <= 30):
        valida = True
elif mes == 2:
    # Testa se é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if (dia <= 29):
            valida = True
    elif (dia <= 28):
        valida = True

if (valida):
    print('Data válida')
else:
    print('Inválida')


