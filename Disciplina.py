class Disciplina:
    def __init__(self, nome, coddisciplina):
        self.nome = nome
        self.coddisciplina = coddisciplina
        self.nota = 0
    def disciplinas(self):
        print('Acesso a lista de disciplinas pelo código:', self.coddisciplina)
    def getdisciplina(self):
        print('Nota total das disciplinas:', self.nota)
    def setdisciplina(self, n):
        self.nota = n
        print('Nota atual da media das disciplinas:', self.nota)
    def mostradisciplina(self):
        print(f'A disciplina: {self.nome}, com o código: {self.coddisciplina}')
disciplina = Disciplina('TI', 3869)
disciplina.mostradisciplina()
disciplina.disciplinas()
disciplina.getdisciplina()
disciplina.setdisciplina(10)

