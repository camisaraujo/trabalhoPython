class Funcionario:
    def __init__(self, nome: str, salario: float, aumento: float):
        self.nome = nome
        self.salario = salario 
        self.aumento = aumento 

    def aumentarSalario(self, aumento):
        self.salario += self.salario*aumento/100

    def mostraFuncionario(self):
        print(f'nome: {self.nome}, salario: {self.salario}, aumeto: {self.aumento}')
        
func = Funcionario('Maria', 1500, 100)
func.mostraFuncionario()
func.aumentarSalario(1000)
func.mostraFuncionario()