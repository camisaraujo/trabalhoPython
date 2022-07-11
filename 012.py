class Cliente:
    def __init__(self, nome, idade, sexo, salario):
        self.nome = str(nome)
        self.idade = int(idade)
        self.sexo = str(sexo)
        self.salario = float(salario)
        print(nome, idade, sexo, salario)

    def getSalario(self):
        print('O preço original do salario é :', self.salario)
    #Método para alterar o preço do salário 
    def setSalario(self, salarioNovo):
        self.salario = salarioNovo
        print('O novo preço do salário é :', self.salario)

    mostraSalario = property(getSalario, setSalario) 
cliente = Cliente('Camis', 19, 'Feminino', 1.800)
cliente.getSalario()
cliente.setSalario(1.900)
print(vars(cliente))   
