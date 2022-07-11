class Funcionario:
    def _init_(self, nome: str, cpf: str, salario: float, desconto: float, salarioliquido: float):
        self.desconto = desconto
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.salarioliquido = salarioliquido

    def descontar(self, salario, desconto, salarioliquido):
        self.desconto = (salario * 0.05)
        salarioliquido = salario - desconto

    def mostraFuncionario(self):
        print(f'Desconto: {self.desconto}, nome: {self.nome}, cpf: {self.cpf}, salario: {self.salario}, salarioliquido: {self.salarioliquido}')

marcos = Funcionario('Marcos', 2500, 0.05, 2375) 
marcos.mostraFuncionario()
marcos.descontar(3000,0.05) 
marcos.liquidar(3000,1,1)
marcos.mostraFuncionario()    