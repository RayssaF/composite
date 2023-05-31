from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def getPreco(self):
        pass

class ProdutoSimples(Produto):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def getPreco(self):
        return self.preco

class ProdutoComposto(Produto):
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def addProduto(self, produto):
        self.produtos.append(produto)

    def removeProduto(self, produto):
        self.produtos.remove(produto)

    def getPreco(self):
        PrecoTotal = 0
        for produto in self.produtos:
            PrecoTotal += produto.getPreco()
        return PrecoTotal

# Criando produtos individuais
produto1 = ProdutoSimples("Produto 1", 10)
produto2 = ProdutoSimples("Produto 2", 5)
produto3 = ProdutoSimples("Produto 3", 3)
produto4 = ProdutoSimples("Produto 4", 6)


# Criando produtos compostos
composite1 = ProdutoComposto("Composite 1")
composite1.addProduto(produto1)
composite1.addProduto(produto2)

composite2 = ProdutoComposto("Composite 2")
composite2.addProduto(produto3)
composite2.addProduto(produto4)

# Adicionando produtos individuais e produtos compostos
composite2.addProduto(composite1)

# Obtendo o preço total do produto composto
PrecoTotal = composite2.getPreco()
print(f"Preço total do produto composto: R$ {PrecoTotal}")