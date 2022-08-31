'''
Crie um arquivo de teste,
crie um objeto da classe Livro e insira os valores informados neste objeto e
mostre os dados do objeto criado.
'''

from livro import Livro

libro = Livro(titulo='MyCanv', autor='Hitler', paginas='132', preco = -20)

print(libro.titulo, libro.autor, libro.paginas, libro.preco)

'''
Crie uma classe chamada Data com os seguintes atributos: dia(int), mes(int), ano(int).  
Encapsule estes atributos (utilize todas as técnicas aprendidas).
Nos métodos “setter” faça validações para não permitir dias , meses e anos inválidos. 
A classe deve possuir ainda um método para retornar a data no formato “20/08/2021”.
'''