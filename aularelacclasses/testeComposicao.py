from composicao import Revistas,Edicao

revista = Revistas(1, 'Veja', 'Política')

revista.setEdicao(1, '2022-03-09', 10)

print(revista.edicao.dataEdicao)