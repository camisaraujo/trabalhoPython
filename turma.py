class Turma:
    def __init__(self, codturma, nometurma):
        self.codturma = int(codturma)
        self.nometurma = str(nometurma)
    def montarturma(self, codturma):
        self.codturma = codturma
    def definirhorario(self, codturma):
        self.codturma = codturma
    def organizarturma(self, codturma):
        self.codturma = codturma
    def mostraturma(self):
        print(f'Codturma: {self.codturma}, Nometurma: {self.nometurma}')
turma = Turma(4, 'TI-Apredizagem')
turma.mostraturma()
turma.montarturma(3)
turma.organizarturma(5)
turma.mostraturma()
