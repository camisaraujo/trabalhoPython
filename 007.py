class Cliente:
    def __init__(self, nome, telefone):
        self.nome = str(nome)
        self.telefone = str(telefone)

class Conta:
    def __init__(self, numero, saldo, limite):
        self.numero = str(numero)
        self.saldo = saldo
        self.limite = limite
        # inicia extrato
        self.extrato = []

    def saque(self,valor):
        if valor < (self.saldo + self.limite):
            self.saldo -= valor 

    def mostraCliente(self):
        print(f'nome: {self.nome}, telefone: {self.telefone}, numero: {self.numero}, saldo: {self.saldo}, limite: {self.limite}')

teste = Cliente('Ana', '90999-0000', 10029, 100.45, 3000,00)

teste.mostraCliente()
