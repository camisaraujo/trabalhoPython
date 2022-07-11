class Curso:
    def __init__(self, codcurso, nomecurso, codturma, coddisciplina):
            self.codcurso = codcurso
            self.nomecurso = nomecurso
            self.codturma = codturma
            self.coddisciplina = coddisciplina
    def montarcurso(self, codcurso):
        self.codcurso = codcurso
    def organizarcurso(self,codturma):
        self.codturma = codturma
    def mostracurso(self):
        print(f'Codcurso: {self.codcurso}, Nome curso: {self.nomecurso}, Codturma: {self.codturma}, Coddisciplina: {self.coddisciplina}')
curso = Curso(1, 'TI-Programação', 2, 1)
curso.mostracurso()
curso.montarcurso(2)
curso.organizarcurso(4)
curso.mostracurso()