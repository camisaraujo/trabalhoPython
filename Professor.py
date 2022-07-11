class Professor:
    def __init__(self, codprofessor, nomeprofessor, coddisciplina, nota):
        self.codprofessor = int(codprofessor)
        self.nomeprofessor = str(nomeprofessor)
        self.coddisciplina = int(coddisciplina)
        self.nota = int(nota)

    def definirprofessor(self, codprofessor):
        self.codprofessor = codprofessor
    def notas(self, nota):
        self.nota = nota
    def mostraprofessor(self):
        print(f'Codprofessor: {self.codprofessor}, Nomeprofessor: {self.nomeprofessor}, Coddisciplina: {self.coddisciplina}, Nota: {self.nota}')

professor = Professor(1, 'Ana', 3, 0)
professor.mostraprofessor()
professor.definirprofessor(3)
professor.notas(6)
professor.mostraprofessor()