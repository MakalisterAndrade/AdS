"""
Makalister Andrade da Silva - UTF8 - 06-06-2022


"""

# 01 - Implementando lista simplesmente encadeada - com encadeamento circular
#- Defina a classe no;
#- Crie o método construtor que recebe os parâmetros, self e valor;
#- Crie os atributos valor e classe

class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None



# 1.2 – Defina a classe lista circular:
# 1.2.1 - Crie o método construtor, que recebe o parâmetro self;
#- Crie os atributos de instância primeiro e último que recebem Nome
#- Estes são os ponteiros de referência de nossa lista;

class Lista_Enc_Circular:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.valor = None




# 1.2.2 - Crie o método que verifica se a lista está vazia;
    def pesquisaObjeto(self, valor):
        if self.primeiro == None:
            print('Lista vazia')
            return None

# 1.2.3 - Crie o método que insere objeto no início da lista, passando como
#parâmetro valor. Não esqueça de verificar se a lista está vazia, pois se
#for verdade este será o primeiro nó. Se não o procedimento de inserção
#de novos nós será outro.

        atualiza = self.primeiro
        while atualiza.valor != valor:
            if atualiza.proximo == None:
                return None
            else:
                atualiza = atualiza.proximo
        return atualiza

# 1.2.4 - Crie o método que insere objeto no final da lista, passando como parâmetro valor;


        atualiza = self.ultimo
        while atualiza.valor != valor:
            if atualiza.ultimo == None:
                return None
            else:
                atualiza = atualiza.ultimo
        return atualiza

    def mostrar(self, valor):
        print(self.valor)


# 1.2.5 Crie o método que insere objeto no final da lista, passando como parâmetro valor;

# 1.2.6 – Instancie o objeto do tipo lista circular;

circ = Lista_Enc_Circular()

# 1.2.7 – Insira 5 objetos no final da lista circular;
circ.ultimo = 'pescador', 'borboleta', 'cego', 'nove', 'oito', 'orelha de coelho'
print()
print(circ.ultimo)

#1.2.8 — Insira 3 objetos no início da lista circular;
circ.primeiro = 'bowen', 'bachmann',   'boca de lobo'
print()
print(circ.primeiro)
# 1.2.9 – Mostre na tela os elementos da lista circular – loop infinito;
print()
print(circ.primeiro, circ.ultimo)

# 1.2.10 – Mostre na tela os elementos da lista circular – sem loop infinito;
print(circ.primeiro, circ.ultimo)