class Livro:
    def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = str(nome)
        self.qtdPaginas = int(qtdPaginas)
        self.autor = str(autor)
        self.preco = float(preco)
        print(nome, qtdPaginas, autor, preco)

    def getPreco(self):
        print('O preco Original do livro é :', self.preco)
    #Método para alterar o preço do livro
    def setPreco(self, precoNovo):
        self.preco = precoNovo
        print('O novo preco do livro é :', self.preco)

    mostraLivro = property(getPreco, setPreco)
livro = Livro('Livro A', 320, 'Luis Peixoto', 25)
livro.getPreco()
livro.setPreco(15)
print(vars(livro))
