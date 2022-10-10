from agregacao import Produto, Carrinho

produto1 = Produto(1, 'Moedor de carne', 33.43, 200)
produto2 = Produto(2, 'Jujuba', 2.45, 100)
produto3 = Produto(3, 'KitKat', 4.60, 30)

carrinho = Carrinho()
carrinho.itens = produto1
carrinho.itens = produto2
carrinho.itens = produto3
carrinho.itens = produto2
carrinho.itens = produto1

carrinho.exibeCarrinho()

carrinho.itens = produto3
carrinho.fecharCompra()
