from ex1 import Editora, Livro


editora1 = Editora(1, 'Editora Ifro', 'Menino Pimpão', '6995544221')

livro1 = Livro(editora1, 1, 'Obstinada','123456789')
print(type(livro1.editora))
print()
print(dir(livro1.editora))
print()
print(livro1.editora.razaoSocial)
